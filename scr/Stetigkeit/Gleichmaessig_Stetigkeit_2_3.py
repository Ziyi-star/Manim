from manim import *

class gleichmassigStetigkeitTwoThree(ZoomedScene):
    def __init__(self, **kwargs):
        ZoomedScene.__init__(
        self,
        zoom_factor=0.3,
        zoomed_display_height=5,
        zoomed_display_width=3,
        image_frame_stroke_width=20,
        zoomed_camera_config={
            "default_frame_stroke_width": 3,
        },
        **kwargs
    )
    def animate_scene_with_zoom(self, target_x, target_delta):
        """
        Animates scene with x movement and delta change, including zoom functionality
        Args:
            target_x (float): Target value for x_tracker
            target_delta (float): New delta value to set
        """
        # Animate x movement
        self.play(
            self.x_tracker.animate.set_value(target_x),
            run_time=3,
            rate_func=linear
        )
        self.wait(1)

        # Handle zoom functionality
        self.remove(self.highlighted_graph)

        # Update delta and related elements
        delta = target_delta
        self.math_text_delta.become(
            MathTex(f"\\delta = {target_delta}").next_to(self.math_text_epsilon, DOWN).set_color(PURPLE)
        )
        self.moving_delta_box.become(
            Rectangle(
                width=target_delta * self.axes.x_axis.unit_size,
                height=1.5 * self.axes.y_axis.unit_size, 
                color=PURPLE,
                fill_opacity=0.4,
                stroke_width=2
            ).move_to(self.axes.coords_to_point(self.x_tracker.get_value(), self.func(self.x_tracker.get_value())))
        )
        self.wait(1)

        self.activate_zooming(animate=False)
        self.zoomed_camera.frame.set_stroke(width=0)
        self.zoomed_camera.frame.add_updater(
            lambda f: f.move_to(self.axes.coords_to_point(self.x_tracker.get_value(), self.func(self.x_tracker.get_value())))
        )
        self.play(
            self.zoomed_camera.frame.animate.set_stroke(width=3),
        )
        self.wait(2)
        # Cleanup zoom
        self.zoomed_camera.frame.clear_updaters()
        self.remove(self.zoomed_display, self.zoomed_camera.frame)
        self.wait(2)

    def construct(self):
        # Background settings
        grid = NumberPlane(
            background_line_style={
                "stroke_color": BLUE_D,
                "stroke_width": 1,
                "stroke_opacity": 0.6,
            },
            axis_config={
                "stroke_color": BLUE_D,
                "stroke_width": 1,
                "stroke_opacity": 0.6,
            },
        )

        axes = Axes(
            x_range=[0, 9, 1],
            y_range=[0, 6, 1],
            axis_config={"color": WHITE},
            tips=True
        ).add_coordinates()

        def func(x):
            return 1/x

        # Create the graph of f(x) = 1/x
        graph = axes.plot(
            func,
            x_range=[0.2, 8],  # Avoid x=0 since function is undefined there
            color=BLUE
        )


        # Create me 2 boxes with epsilon and delta in the point (1,1)
        epsilon = 0.3
        delta = 0.5
        # Create a ValueTracker for the x coordinate
        x_tracker = ValueTracker(1.5)

         #Label epsilon and delta at top right corner
        math_text_epsilon = MathTex(r"\epsilon = 0.3").set_color(ORANGE)
        math_text_epsilon.to_corner(UR)
        math_text_delta = MathTex(r"\delta = 0.5").next_to(math_text_epsilon, DOWN).set_color(PURPLE)
        math_text_X = always_redraw(
            lambda: MathTex(
                r"\mathbf{x = " + f"{x_tracker.get_value():.2f}" + "}"
            )
            .set_color(WHITE)
            .next_to(math_text_delta, DOWN)
        )

        # the graph between moving_epsilon_box and moving_delta_box are marked
        # Create highlighted section of the graph
        highlighted_graph = always_redraw(
            lambda: axes.plot(
                func,
                x_range=[
                    x_tracker.get_value() - delta/2,
                    x_tracker.get_value() + delta/2
                ],
                color=RED,
                stroke_width=3
            )
        )
        in_Schnitt = always_redraw(
            lambda: VGroup(*[
                Dot(
                    axes.coords_to_point(x, func(x)),
                    color=YELLOW,
                    radius=0.01
                )
                for x in np.linspace(
                    x_tracker.get_value() - delta/2,
                    x_tracker.get_value() + delta/2,
                    100
                )
                if (abs(func(x) - func(x_tracker.get_value())) <= epsilon/2)
            ])
        )

       
        moving_epsilon_box = always_redraw(
            lambda: Rectangle(
                width=1.5 * axes.x_axis.unit_size,
                height=epsilon * axes.y_axis.unit_size,
                color=ORANGE,
                fill_opacity=0.4,
                stroke_width=2
            ).move_to(axes.coords_to_point(x_tracker.get_value(), func(x_tracker.get_value())))
        )
        moving_delta_box = always_redraw(
            lambda: Rectangle(
                width=delta * axes.x_axis.unit_size,
                height=1.5 * axes.y_axis.unit_size, 
                color=PURPLE,
                fill_opacity=0.4,
                stroke_width=2
            ).move_to(axes.coords_to_point(x_tracker.get_value(), func(x_tracker.get_value())))
        )
        
        # Make variables class attributes
        self.func = func
        self.axes = axes
        self.x_tracker = x_tracker
        self.delta = delta
        self.math_text_epsilon = math_text_epsilon
        self.math_text_delta = math_text_delta
        self.moving_delta_box = moving_delta_box
        self.highlighted_graph = highlighted_graph

        # Add elements to the scene
        self.add(grid, axes, graph)
        self.add(math_text_epsilon, math_text_delta, math_text_X)
        self.add(moving_epsilon_box, moving_delta_box)
        self.add(highlighted_graph, in_Schnitt)
        
        # Scene 1:
        self.animate_scene_with_zoom(target_x=1.10, target_delta=0.4)

        #Scene 2:

