from manim import *

class gleichmassigStetigkeitTwo(Scene):
    # draw the graph of the function f(x) 1/x in x range (0,9)
    def construct(self):
         # Background grid
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


        #Label epsilon and delta = 1/2 at top right corner
        math_text_epsilon = MathTex(r"\epsilon = 0.3").set_color(ORANGE)
        math_text_epsilon.to_corner(UR)
        math_text_delta = MathTex(r"\delta = 0.5").next_to(math_text_epsilon, DOWN).set_color(PURPLE)

        # Create me 2 boxes with epsilon and delta in the point (1,1)
        epsilon = 0.3
        delta = 0.5
        # Create a ValueTracker for the x coordinate
        x_tracker = ValueTracker(1.5)
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
                stroke_width=6
            )
        )
        in_Schnitt = always_redraw(
            lambda: VGroup(*[
                Dot(
                    axes.coords_to_point(x, func(x)),
                    color=YELLOW,
                    radius=0.03
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
                height=4 * axes.y_axis.unit_size, 
                color=PURPLE,
                fill_opacity=0.4,
                stroke_width=2
            ).move_to(axes.coords_to_point(x_tracker.get_value(), func(x_tracker.get_value())))
        )

        # Add elements to the scene
        self.add(grid, axes, graph)
        self.add(math_text_epsilon, math_text_delta)
        self.add(moving_epsilon_box, moving_delta_box)
        self.add(highlighted_graph, in_Schnitt)
        
        # Animate the movement
        self.play(
            x_tracker.animate.set_value(0.5),
            run_time=6,  # Longer runtime for slower movement
            rate_func=linear
        )
        
        self.wait(1)
