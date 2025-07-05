from manim import *
from matplotlib import axes

class NullstellenRekursion(Scene):
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

        # Funktion Animation
        # Create axes for the graph on the right
        axes = Axes(
            x_range=[-3.5, 3.5, 1],
            y_range=[-23, 23, 5],
            y_length=10,
            x_length=12,
            axis_config={"include_numbers": True, "font_size": 24}
        ).scale(0.75).to_edge(LEFT, buff=5)

        # Define a function for the graph
        def func(x):
            return x**3 - 2*x + 2

        # Plot the function
        graph = axes.plot(func, x_range=[-3, 3], color=BLUE)
        label_graph = axes.get_graph_label(
            graph, 
            label="f(x)", 
            x_val=3.2,  # Position where label appears
            direction=LEFT * 1.5,
            color=BLUE
        ).scale(0.6)


        # Add text and graph to the scene
        self.add(grid,axes)
        self.play(Create(graph), run_time=2)
        self.play(Write(label_graph), run_time=1.5)
        self.wait(1.5)
