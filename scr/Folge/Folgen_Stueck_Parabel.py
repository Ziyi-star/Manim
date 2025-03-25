from manim import *

config.background_color = WHITE

class FolgenStueckParabel(Scene):
    def construct(self):
        # Axes setup with numbers
        axes = Axes(
            x_range=[-1, 5, 1],
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
        graph = axes.plot(func, color=GREEN, x_range=[0, 3])

        self.add(axes)
        self.play(Create(graph), run_time=2)
        self.wait(1)

        # TODO: Diskrete Dote in 1,2,3 machen
        # Create discrete dots at points (1,1), (2,4), (3,9)
        dots = VGroup()
        points = [(1,func(1)), (2,func(2)), (3,func(3))]
        
        for x, y in points:
            dot = Dot(axes.c2p(x, y), color=BLACK)
            dots.add(dot)
        self.play(Create(dots), run_time=2)
        self.wait(2)
        self.remove(graph)
        self.wait(2)

        # TODO: Aus Graph auszoomen Diskrete Dote in 1,2,3 bis 10 machen
         # Create zoomed out axes
        zoomed_axes = Axes(
            x_range=[-1, 11, 1],
            y_range=[-1, 110, 10],
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

        # Create more dots from 1 to 10
        more_dots = VGroup()
        more_points = [(x, func(x)) for x in range(1, 11)]
        
        for x, y in more_points:
            dot = Dot(zoomed_axes.c2p(x, y), color=BLACK)
            more_dots.add(dot)

        # Animate transition
        self.play(
            Transform(axes, zoomed_axes),
            Transform(dots, more_dots),
            run_time=2
        )
        self.wait(4)