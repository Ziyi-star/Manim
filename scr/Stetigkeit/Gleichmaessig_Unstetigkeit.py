from manim import *

class GleichmassigUnstetigkeitZoom(ZoomedScene):
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

        epsilon = 0.5
        delta_tracker = ValueTracker(0.5)
        x_tracker = ValueTracker(1)

        # Moving boxes
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
                width=delta_tracker.get_value() * axes.x_axis.unit_size,
                height=3 * axes.y_axis.unit_size,
                color=PURPLE,
                fill_opacity=0.4,
                stroke_width=2
            ).move_to(axes.coords_to_point(x_tracker.get_value(), func(x_tracker.get_value())))
        )

        # Two Dots around delta
        left_dot = always_redraw(
            lambda: Dot(
                point=axes.coords_to_point(
                    x_tracker.get_value() - delta_tracker.get_value()/2,
                    func(x_tracker.get_value() - delta_tracker.get_value()/2)
                ),
                color=RED,
                radius=0.1
            )
        )
        right_dot = always_redraw(
            lambda: Dot(
                point=axes.coords_to_point(
                    x_tracker.get_value() + delta_tracker.get_value()/2,
                    func(x_tracker.get_value() + delta_tracker.get_value()/2)
                ),
                color=GREEN,
                radius=0.1
            )
        )

        # Label epsilon and delta
        math_text_epsilon = MathTex(r"\epsilon = 0.5").set_color(ORANGE).to_corner(UR)
        # Replace the static math_text_delta with:
        math_text_delta = always_redraw(
            lambda: MathTex(r"\delta = {:.1f}".format(delta_tracker.get_value()))
            .set_color(PURPLE)
            .next_to(math_text_epsilon, DOWN)
        )

        # Add main objects
        self.add(grid, axes, graph, moving_epsilon_box, moving_delta_box, left_dot, right_dot, math_text_epsilon, math_text_delta)

        # Animate x and delta trackers
        self.play(
            x_tracker.animate.set_value(0.4),
            delta_tracker.animate.set_value(0.05),
            run_time=6,
            rate_func=linear
        )
        self.wait(2)

        

