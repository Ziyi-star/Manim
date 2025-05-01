from manim import *

class gleichmassigStetigkeit(Scene):
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

        # Labels
        #function_label = MathTex("f(x)=\\frac{1}{x}").next_to(graph, UP)

        #Label epsilon and delta = 1/2 at top right corner
        math_text_epsilon = MathTex(r"\epsilon = 1").set_color(ORANGE)
        math_text_epsilon.to_corner(UR)
        math_text_delta = MathTex(r"\delta = 1")
        math_text_delta.next_to(math_text_epsilon, DOWN).set_color(PURPLE)

        # Create me 2 boxes with epsilon and delta in the point (1,1)
        epsilon = 1
        delta = 1
        # Create a ValueTracker for the x coordinate
        x_tracker = ValueTracker(1.5)
        moving_point = axes.coords_to_point(x_tracker.get_value(), func(x_tracker.get_value()))
        # Define moving dots using always_redraw
        moving_dot_left = always_redraw(
            lambda: Dot(
                point=axes.coords_to_point(
                    x_tracker.get_value() - 0.4,
                    func(x_tracker.get_value() - 0.4)
                ),
                color=RED
            )
        )

        moving_dot_right = always_redraw(
            lambda: Dot(
                point=axes.coords_to_point(
                    x_tracker.get_value() + 0.4,
                    func(x_tracker.get_value() + 0.4)
                ),
                color=GREEN
            )
        )

        moving_epsilon_box = always_redraw(
            lambda: Rectangle(
                width=3 * axes.x_axis.unit_size,
                height=epsilon * axes.y_axis.unit_size,
                color=ORANGE,
                fill_opacity=0.4,
                stroke_width=2
            ).move_to(axes.coords_to_point(x_tracker.get_value(), func(x_tracker.get_value())))
        )
        moving_delta_box = always_redraw(
            lambda: Rectangle(
                width=delta * axes.x_axis.unit_size,
                height=3 * axes.y_axis.unit_size,
                color=PURPLE,
                fill_opacity=0.4,
                stroke_width=2
            ).move_to(axes.coords_to_point(x_tracker.get_value(), func(x_tracker.get_value())))
        )

        # Add elements to the scene
        self.add(grid, axes, graph)
        self.add(math_text_epsilon, math_text_delta)
        self.add(moving_dot_left, moving_dot_right, moving_epsilon_box, moving_delta_box)
        
        # Animate the movement
        self.play(
            x_tracker.animate.set_value(7.5),
            run_time=10,
            rate_func=linear
        )
        self.wait(1)
