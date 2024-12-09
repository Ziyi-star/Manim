from manim import *

class Trigonometrie(Scene):
    def construct(self):
        # Axes for sine and cosine functions
        axes = Axes(x_range=[0, TAU], y_range=[-1.5, 1.5], axis_config={"include_tip": True})
        sine_graph = axes.plot(lambda x: np.sin(x), color=BLUE, x_range=[0, TAU])
        cosine_graph = axes.plot(lambda x: np.cos(x), color=RED, x_range=[0, TAU])

        # Labels
        sine_label = MathTex("\\sin(x)").set_color(BLUE).next_to(axes, UP)
        cosine_label = MathTex("\\cos(x)").set_color(RED).next_to(axes, DOWN)

        # Display sine and cosine graphs
        self.play(Create(axes), Create(sine_graph), Write(sine_label))
        self.play(Create(cosine_graph), Write(cosine_label))
        self.wait()
