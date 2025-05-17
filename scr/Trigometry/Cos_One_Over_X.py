from manim import *
import numpy as np

class CosOneOverXZoom(Scene):
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
            axis_config={
                "include_numbers": True,
                "numbers_to_include": [-1.0, -0.5, 0.0, 0.5, 1.0]
            }
        )

        # Funktion definieren: cos(1/x), mit Abfangen von x=0
        def func(x):
            if x == 0:
                return 0
            return np.cos(1 / x)

        graph = axes.plot(func, x_range=[-1, 1], color=BLUE)

        self.add(grid)
        self.play(Create(axes), run_time=2)
        self.play(Create(graph), run_time=5)
        self.wait(2)
