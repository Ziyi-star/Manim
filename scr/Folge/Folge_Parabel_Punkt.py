from manim import *

class FolgeParabelPunkt(Scene):
    def construct(self):
        # Create axes
        axes = Axes(
            x_range=[-4, 5, 1],
            y_range=[0, 9, 1],
            axis_config={"color": BLUE},
        )

        # Create labels for the axes
        labels = axes.get_axis_labels(x_label="x", y_label="y")

        # Create the graph of the function f(x) = x^2
        graph = axes.plot(lambda x: x**2, color=YELLOW)

        # Create a label for the graph
        graph_label = MathTex("f(x) = x^2").next_to(graph, UP)

        # Animate the creation of the axes and labels
        self.play(Create(axes), Write(labels))

        # Animate the drawing of the graph
        self.play(Create(graph), Write(graph_label))

        # Wait for a moment before ending the scene
        self.wait(2)

# To run this code, save it in a Python file and execute it using Manim.
# Example command: manim -pql your_file.py AnimateGraph