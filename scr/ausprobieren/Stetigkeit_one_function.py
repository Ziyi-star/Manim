from manim import *

class Stetigkeit_one_function(Scene):
    def construct(self):
        # Create the axes
        axes = Axes(
            x_range=[-1, 7, 1],  # Range of x-axis
            y_range=[-2, 3, 1],  # Range of y-axis
            x_length=10,         # Length of the x-axis
            y_length=6,          # Length of the y-axis
            axis_config={"include_tip": False},  # No default arrow tips
        )

        # Add x-axis and y-axis labels
        labels = axes.get_axis_labels(x_label="x", y_label="y")


        # Plot the yellow curve
        func = axes.plot(
            lambda x: 0.5 * np.sin(2 * x) - 0.2 * x + 1,  # Function for the curve
            color=YELLOW,
            x_range=[0, 6],  # Plot range
        )

        # Add a circular highlight around the curve
        circle_position = axes.coords_to_point(2, func.underlying_function(2))
        circle = Circle(radius=0.1, color=YELLOW).move_to(circle_position)



        # Add a yellow dot on the curve
        dot_position = axes.coords_to_point(3, func.underlying_function(3))  # Example (x=3, y=0.5)
        dot = Dot(dot_position, color=YELLOW)



        # Add elements to the scene
        self.play(Create(axes), Write(labels))
        self.play(Create(func))
        self.play(FadeIn(dot), Create(circle))
        self.wait()
