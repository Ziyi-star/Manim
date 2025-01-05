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
            x_range=[-1, 3, 0.5],
            y_range=[0, 5, 1],
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="f(x)")

        # Function definition
        def func(x):
            return 0.5 * x**2 + 1

        # Function graph
        graph = axes.plot(func, color=GREEN)

         # Add all elements to the scene
        self.add(grid)  # Add the NumberPlane as the background
        self.play(Create(axes), Write(axes_labels))
        self.play(Create(graph))
        self.wait(2)
        