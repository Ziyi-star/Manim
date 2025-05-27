from manim import *

class UngleichmassigStetigkeitZoom(ZoomedScene):
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

    def construct(self):
        # Set up grid and axes
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

        graph = axes.plot(
            func,
            x_range=[0.2, 8],
            color=BLUE
        )

        epsilon = 0.3
        delta_tracker = ValueTracker(0.3)
        x_tracker = ValueTracker(1)

        highlighted_graph = always_redraw(
            lambda: axes.plot(
                func,
                x_range=[
                    x_tracker.get_value() - delta_tracker.get_value()/2,
                    x_tracker.get_value() + delta_tracker.get_value()/2
                ],
                color=YELLOW,
                stroke_width=6
            )
        )

        # Moving boxes
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
                width=delta_tracker.get_value() * axes.x_axis.unit_size,
                height=1.5 * axes.y_axis.unit_size,
                color=PURPLE,
                fill_opacity=0.4,
                stroke_width=2
            ).move_to(axes.coords_to_point(x_tracker.get_value(), func(x_tracker.get_value())))
        )

        # Label epsilon and delta
        math_text_epsilon = MathTex(r"\epsilon = 0.3").set_color(ORANGE).to_corner(UR).shift(LEFT * 4)
        math_text_delta = always_redraw(
            lambda: MathTex(
                "\\mathbf{\\delta = " + f"{delta_tracker.get_value():.2f}" + "}"
            )
            .set_color(PURPLE)
            .next_to(math_text_epsilon, DOWN)
        )

        # Add main objects
        self.add(grid, axes, graph, moving_epsilon_box, highlighted_graph, moving_delta_box, math_text_epsilon, math_text_delta)

        # Animate x and delta trackers
        self.activate_zooming(animate=False)
        # Make frame invisible
        self.zoomed_camera.frame.set_stroke(width=0)
        self.zoomed_camera.frame.add_updater(
            lambda f: f.move_to(axes.coords_to_point(x_tracker.get_value(), func(x_tracker.get_value())))
        )
        self.wait(1)
        self.play(
            self.zoomed_camera.frame.animate.set_stroke(width=3),
        )
        self.play(
            x_tracker.animate.set_value(0.4),
            delta_tracker.animate.set_value(0.06),
            run_time=6,
            rate_func=linear
        )
        self.wait(2)

        

