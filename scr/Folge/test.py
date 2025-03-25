from manim import *

config.background_color = WHITE

class CircleFlip(Scene):
    def construct(self):
        axis = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            tips=False
        ).add_coordinates()
        self.add(axis)
