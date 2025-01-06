from manim import *

class EpsilonDeltaVisualization(Scene):
    def construct(self):
        # Axes setup
        axes = Axes(
            x_range=[-1, 3, 0.5],
            y_range=[0, 5, 1],
            axis_config={"include_numbers": True}
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="f(x)")

        # Function definition
        def func(x):
            return 0.5 * x**2 + 1

        # Function graph
        graph = axes.plot(func, color=GREEN, label="f(x)")

        # x0 and f(x0)
        x0 = 1.5
        fx0 = func(x0)

        # Mark x0 and f(x0)
        x0_dot = Dot(axes.coords_to_point(x0, fx0), color=RED)
        x0_label = MathTex("x_0").next_to(x0_dot, DOWN)
        fx0_label = MathTex("f(x_0)").next_to(x0_dot, LEFT)

        # Delta (δ) lines
        delta = 0.5
        x0_minus_delta = axes.coords_to_point(x0 - delta, 0)
        x0_plus_delta = axes.coords_to_point(x0 + delta, 0)
        delta_lines = VGroup(
            DashedLine(x0_minus_delta, axes.coords_to_point(x0 - delta, fx0), color=BROWN),
            DashedLine(x0_plus_delta, axes.coords_to_point(x0 + delta, fx0), color=BROWN)
        )
        delta_label = MathTex("\\delta").next_to(delta_lines, DOWN)

        # Epsilon (ε) lines
        epsilon = 0.8
        fx0_minus_epsilon = axes.coords_to_point(0, fx0 - epsilon)
        fx0_plus_epsilon = axes.coords_to_point(0, fx0 + epsilon)
        epsilon_lines = VGroup(
            DashedLine(fx0_minus_epsilon, axes.coords_to_point(x0, fx0 - epsilon), color=TURQUOISE),
            DashedLine(fx0_plus_epsilon, axes.coords_to_point(x0, fx0 + epsilon), color=TURQUOISE)
        )
        epsilon_label = MathTex("\\epsilon").next_to(epsilon_lines, LEFT)

        # Highlight delta and epsilon regions
        delta_region = axes.get_area(graph, x_range=[x0 - delta, x0 + delta], color=BROWN, opacity=0.2)
        epsilon_region = Rectangle(
            width=axes.c2p(x0 + delta, 0)[0] - axes.c2p(x0 - delta, 0)[0],
            height=axes.c2p(0, fx0 + epsilon)[1] - axes.c2p(0, fx0 - epsilon)[1],
            color=TURQUOISE,
            fill_opacity=0.2,
            stroke_opacity=0.3
        ).move_to(axes.c2p(x0, fx0))

        # Adding all elements to the scene
        self.play(Create(axes), Write(axes_labels))
        self.play(Create(graph))
        self.play(FadeIn(x0_dot, x0_label, fx0_label))
        self.play(Create(delta_lines), Write(delta_label))
        self.play(Create(epsilon_lines), Write(epsilon_label))
        self.play(FadeIn(delta_region, epsilon_region))

        # Wait before finishing
        self.wait()
