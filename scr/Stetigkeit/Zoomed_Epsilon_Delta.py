from manim import *

class ZoomedEpsilonDelta(ZoomedScene):
    def construct(self):
        # Axes and Graph
        axes = Axes(
            x_range=[-1, 5, 1],
            y_range=[0, 10, 1],
            axis_config={"include_numbers": False}
        ).add_coordinates()
        def func(x):
            return x**2
        graph_func = axes.plot(func, color=GREEN)

        # Marking x0 and f(x0)
        x0, epsilon = 2, 3
        fx0 = func(x0)
        delta = np.sqrt(fx0 + epsilon) - x0

        # Add axes and graph to scene
        self.add(axes, graph_func)

        # Zoom Rectangle