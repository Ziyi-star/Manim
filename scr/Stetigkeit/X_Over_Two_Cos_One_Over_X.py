from manim import *
import numpy as np

class XOverTwoCosOneOverXZoom(ZoomedScene):
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
        # Achsen für den Bereich [-1, 1]
        axes = Axes(
            x_range=[-0.5, 0.5, 0.05], 
            y_range=[-0.04, 0.04, 0.01],
            x_axis_config={
                "include_numbers": True,
                "numbers_to_include": [-0.5, -0.1,0.0, 0.1, 0.5]
            },
            y_axis_config={
                "include_numbers": True,
                "numbers_to_include": [-0.04, 0.04]
            }
        )

        def func(x):
            if x == 0:
                return 0
            return x**2 * np.cos(1 / x)

        math_label = MathTex(r"f(x) = x^2 \cdot \cos\left(\frac{1}{x}\right)").to_corner(UR)

        graph1 = axes.plot(func, x_range=[-0.5, -0.1], color=ORANGE)
        graph2 = axes.plot(func, x_range=[-0.1, 0.1], color=ORANGE, stroke_width=2)
        graph3 = axes.plot(func, x_range=[0.1, 0.5], color=ORANGE)

        self.add(grid)
        self.add(math_label)
        self.play(Create(axes), run_time=2)
        self.play(Create(graph1), run_time=2)
        self.play(Create(graph2), run_time=15)  
        self.play(Create(graph3), run_time=2)
        self.wait(2)

        #Zoom in, length and width here manually adjusted to look pretty
        zoom_rect = Rectangle(
            width=2, height=1, color=YELLOW
        ).move_to(axes.c2p(0, 0))
        self.play(Create(zoom_rect))  # Animate the zoom rectangle
        self.wait(2)
         # Scale the view to focus on the red point
        self.play(self.camera.frame.animate.scale(1/3).move_to(axes.c2p(0, 0)))  # Zoom in
        self.wait(5)
         # Reset the camera to its original position
        self.play(self.camera.frame.animate.scale(3).move_to(ORIGIN))  # Zoom out
        self.wait(2)
