from manim import *
import numpy as np

class CosineCircleRadiant(Scene):
    def construct(self):
        # Create the unit circle
        circle = Circle(radius=2, color=BLUE).to_edge(LEFT, buff=1)
        center = circle.get_center()

        # Value Tracker for the angle in degrees
        angle = ValueTracker(0)
        
        # Create an arrow for the angle
        arrow = always_redraw(lambda: Arrow(
            start=center, 
            end=center + 2 * np.array([
                np.cos(angle.get_value()),  # x = cos(angle in radians)
                np.sin(angle.get_value()),  # y = sin(angle in radians)
                0
            ]), 
            buff=0, 
            color=GREEN
        ))

        # Create the horizontal line for the cosine graph
        horizontal_line = always_redraw(lambda: Line(
            start=center, 
            end=center + 2 * np.array([
                np.cos(angle.get_value()),  # x
                0,  # y
                0
            ]),
            color=YELLOW
        ))

        # Create the vertical dashed line for the cosine graph
        vertical_line = always_redraw(lambda: DashedLine(
            start=center + 2 * np.array([
                np.cos(angle.get_value()), 0, 0
            ]),
            end=center + 2 * np.array([
                np.cos(angle.get_value()), 
                np.sin(angle.get_value()), 
                0
            ]),
            color=WHITE
        ))

        # Create the Axes for the cosine graph
        ax = Axes(
            x_range=[0, TAU, TAU / 4],  # 0 to 2π with steps of π/2
            y_range=[-1.0, 1.0, 1],  # Range for the cosine graph
            x_length=7.5,
            y_length=4,
            axis_config={"color": WHITE},
            tips=True,
        ).next_to(circle, RIGHT, buff=0)

        # Labels for the cosine graph
        x_radian_labels = ax.get_x_axis().add_labels({
            0: MathTex("0"),
            PI / 2: MathTex("\\frac{\\pi}{2}"),
            PI: MathTex("\\pi"),
            3 * PI / 2: MathTex("\\frac{3\\pi}{2}"),
            TAU: MathTex("2\\pi")
        })

        y_degree_labels = ax.get_y_axis().add_labels({
            1: MathTex("1"),
            -1: MathTex("-1")
        })

        # Cosine graph
        cosine_graph_tracker = always_redraw(lambda: ax.plot(
            lambda x: np.cos(x),  # x is already in radians
            x_range=[0, angle.get_value()],  # Range from 0 to the current angle
            color=GREEN,
        ))

        # Add all elements to the scene
        self.add(circle, arrow, ax, cosine_graph_tracker, x_radian_labels, y_degree_labels, horizontal_line, vertical_line)
        
        # Animate the arrow and cosine graph
        #self.play(angle.animate.set_value(TAU), run_time=20, rate_func=linear)  # TAU = 2π
        self.play(angle.animate.set_value(TAU), run_time=5, rate_func=linear)  # TAU = 2π
        self.wait()
