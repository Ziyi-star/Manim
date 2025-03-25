from manim import *

config.background_color = WHITE

class FolgenStueckParabel(Scene):
    def construct(self):
        # Axes setup with numbers
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-1, 10, 1],
             axis_config={
                "color": BLACK,
                "include_numbers": True,
                "include_ticks": True,
                "decimal_number_config": {
                    "color": GRAY_E,
                    "num_decimal_places": 0
                }
            }
        ).add_coordinates()
        # Function definition
        def func(x):
            return x**2
        graph = axes.plot(func, color=GREEN, x_range=[-3, 3])

        self.add(axes)
        self.play(Create(graph), run_time=2)
        self.wait(1)