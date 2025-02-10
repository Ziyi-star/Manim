from manim import *

class MittelwertsatzRolle(Scene):
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
       
        # Axes setup
        axes = Axes(
            x_range=[-1, 7, 1],  # X-axis range
            y_range=[-1, 11, 1],  # Y-axis range
            axis_config={"include_numbers": True},
        ).add_coordinates()

        # Labels for axes
        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("y")

        # Function definition
        def func(x):
            return (1 / 0.9) * (x-0.5) * (x - 2.5) * (x - 4.5) + (x * np.tan(np.radians(60)))
        graph = axes.plot(func, color=BLUE)
        graph_label = axes.get_graph_label(graph, label="f(x)")

        self.play(Create(grid), Create(axes), Create(x_label), Create(y_label), Create(graph), Create(graph_label))
        self.wait(2)
        
        #todo: draw the tangent line at point x = 4.5 of function f(x)
        x0 = 3.6
        fx0 = func(x0)
        x0_fx0_dot = Dot(axes.coords_to_point(x0, fx0),color=RED)
        # Derivative of the function
        def func_derivative(x):
            h = 1e-5
            return (func(x + h) - func(x)) / h
        slope = func_derivative(x0)
        tangent_line = axes.plot(lambda x: slope * (x - x0) + fx0, color=RED, x_range=[2.7, 4.5])

        self.play(Create(x0_fx0_dot))
        self.play(Create(tangent_line))
        self.wait(2)





