from manim import *

class EpsilonDeltaKriteriumStetigkeitIntuition(Scene):
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

        # Axes setup
        axes = Axes(
            x_range=[-1, 5, 0.5],
            y_range=[0, 10, 1],
            axis_config={"include_numbers": True}
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="f(x)")

        # Function definition
        def func(x):
            return 0.5 * x**2 + 0.5

        # Function graph
        graph = axes.plot(func, color=GREEN)

         # x0 and f(x0)
        x0 = 3
        fx0 = func(x0)

        # Mark x0 and f(x0)
        x0_dot = Dot(axes.coords_to_point(x0, fx0), color=RED)

        # Dashed lines from (x0, f(x0)) to axes
        dashed_to_x_axis = DashedLine(
            start=axes.coords_to_point(x0, fx0),
            end=axes.coords_to_point(x0, 0),
            color=BLUE
        )
        dashed_to_y_axis = DashedLine(
            start=axes.coords_to_point(x0, fx0),
            end=axes.coords_to_point(0, fx0),
            color=BLUE
        )

        # Labels for x0 on x-axis and f(x0) on y-axis
        x0_axis_label = MathTex("x_0").next_to(axes.coords_to_point(x0, 0), DOWN)
        fx0_axis_label = MathTex("f(x_0)").next_to(axes.coords_to_point(0, fx0), LEFT)

        # Delta lines
        delta = 0.5

        x0_minus_delta = axes.coords_to_point(x0 - delta, 0)
        x0_plus_delta = axes.coords_to_point(x0 + delta, 0)
        delta_lines = VGroup(
            DashedLine(x0_minus_delta, axes.coords_to_point(x0 - delta, func(x0 - delta)), color=YELLOW),
            DashedLine(x0_plus_delta, axes.coords_to_point(x0 + delta, func(x0 + delta)), color=YELLOW)
        )

        # Highlight delta and epsilon regions
        delta_region = axes.get_area(graph, x_range=[x0 - delta, x0 + delta], color=YELLOW, opacity=0.2)

        # Interval with delta under x-axis
        delta_interval = DoubleArrow(
            start=axes.coords_to_point(x0 - delta, -0.5),
            end=axes.coords_to_point(x0 + delta, -0.5),
            color=YELLOW
        )
        delta_label = MathTex("\\delta").next_to(delta_interval, DOWN)

    
         # Add all elements to the scene
        self.add(grid)  # Add the NumberPlane as the background
        self.play(Create(axes), Write(axes_labels))
        self.play(Create(graph))
        self.play(FadeIn(x0_dot))
        self.play(Create(dashed_to_x_axis), Create(dashed_to_y_axis))
        self.play(Write(x0_axis_label), Write(fx0_axis_label))
        self.play(Create(delta_lines))
        self.play(FadeIn(delta_region))
        self.play(Create(delta_interval), Write(delta_label))
        self.wait(2)
        