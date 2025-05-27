from manim import *
import numpy as np

class CosOneOverXZoom(ZoomedScene):
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
            x_range=[-1.0, 1.2, 0.05],
            y_range=[-2, 2, 0.5],
            x_axis_config={
                "include_numbers": True,
                "numbers_to_include": [-1.0, -0.5, -0.1,0.0, 0.1, 0.5, 1.0]
            },
            y_axis_config={
                "include_numbers": True,
                "numbers_to_include": [-1,1]
            }
        )

        def func(x):
            if x == 0:
                return 0
            return np.cos(1 / x)
        
        math_label = MathTex(r"f(x) = \cos\left(\frac{1}{x}\right)").to_corner(UR)

        graph1 = axes.plot(func, x_range=[-1, -0.1], color=BLUE)
        graph2 = axes.plot(func, x_range=[-0.1, 0.1], color=BLUE, stroke_width=2)
        graph3 = axes.plot(func, x_range=[0.1, 1], color=BLUE)

        self.add(grid)
        self.add(math_label)
        self.play(Create(axes), run_time=2)
        self.play(Create(graph1), run_time=2)
        self.play(Create(graph2), run_time=20)  
        self.play(Create(graph3), run_time=2)
        self.wait(2)

        #Zoom in, length and width here manually adjusted to look pretty
        zoom_rect = Rectangle(
            width=2, height=3.5, color=YELLOW
        ).move_to(axes.c2p(0, 0))
        self.play(Create(zoom_rect))  # Animate the zoom rectangle
        self.wait(2)
         # Scale the view to focus on the red point
        self.play(self.camera.frame.animate.scale(0.5).move_to(axes.c2p(0, 0)))  # Zoom in
        self.wait(5)
         # Reset the camera to its original position
        self.play(self.camera.frame.animate.scale(2).move_to(ORIGIN))  # Zoom out
        self.wait(2)
