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
        #self.wait(2)
        
        #todo: draw the tangent line at point x = 4.5 of function f(x)
        def draw_tangent_line_at(x0):
            fx0 = func(x0)
            x0_fx0_dot = Dot(axes.coords_to_point(x0, fx0), color=RED)
            # Derivative of the function
            def func_derivative(x):
                h = 1e-5
                return (func(x + h) - func(x)) / h
            slope = func_derivative(x0)
            tangent_line = axes.plot(lambda x: slope * (x - x0) + fx0, color=RED, x_range=[x0 - 1, x0 + 1])
            return x0_fx0_dot, tangent_line

        #todo: draw the secant line at point x = 0.5 and x = 4.5 of function f(x)
        def draw_secant_line_at(a, b):
            fx0 = func(a)
            fx1 = func(b)
            x0_fx0_dot = Dot(axes.coords_to_point(a, fx0), color=RED)
            x1_fx1_dot = Dot(axes.coords_to_point(b, fx1), color=RED)
            secant_line = axes.plot(lambda x: (fx1 - fx0) / (b - a) * (x - a) + fx0, color=GREEN, x_range=[a - 1, b + 1])
            return x0_fx0_dot, x1_fx1_dot, secant_line
        
        xa_fxa_dot, xb_fxb_dot, secant_line = draw_secant_line_at(0.7, 4.5)
        self.play(Create(xa_fxa_dot), Create(xb_fxb_dot), Create(secant_line))
        self.wait(2)

         # Draw the tangent line at point x = 3,6 
        x0_fx0_dot_two, tangent_line_two = draw_tangent_line_at(3.6)
        self.play(Create(x0_fx0_dot_two))
        self.play(Create(tangent_line_two))
        self.wait(2)





