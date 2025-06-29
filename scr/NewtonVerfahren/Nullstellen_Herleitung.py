from manim import *

class NullstellenHerleitung(Scene):
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

        # Create axes for the graph on the right
        axes = Axes(
            x_range=[-3, 3.5, 1],
            y_range=[-12, 12.5, 2.5],
            axis_config={"include_numbers": True}
        ).scale(0.75).to_edge(LEFT, buff=5)

        # Define a function for the graph
        def func(x):
            return x**3 - 2*x + 2

        # Plot the function
        graph = axes.plot(func, x_range=[-2.6, 2.6], color=BLUE)

        # Add text and graph to the scene
        self.add(grid, axes, graph)
        self.wait(1)