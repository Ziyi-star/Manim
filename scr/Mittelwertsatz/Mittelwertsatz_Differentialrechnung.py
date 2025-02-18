from manim import *

class MittelwertsatzDifferentialrechnung(Scene):
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
        )

        # Labels for axes
        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("y")

        # Function definition
        def func(x):
            return (1 / 0.9) * (x-0.5) * (x - 2.5) * (x - 4.5) + (x * np.tan(np.radians(60)))
        
        graph = axes.plot(func, color=BLUE)
        graph_label = axes.get_graph_label(graph, label="f(x)").scale(0.7)

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
        
        #secant line from point a,to point b
        def draw_secant_line_at(a, b):
            fx0 = func(a)
            fx1 = func(b)
            x0_fx0_dot = Dot(axes.coords_to_point(a, fx0), color=RED)
            x1_fx1_dot = Dot(axes.coords_to_point(b, fx1), color=RED)
            secant_line = axes.plot(lambda x: (fx1 - fx0) / (b - a) * (x - a) + fx0, color=GREEN, x_range=[a - 1, b + 1])
            return x0_fx0_dot, x1_fx1_dot, secant_line


        # Animation
        self.play(Create(grid))
        self.wait(1)
        self.play(Create(axes), Create(x_label), Create(y_label))
        self.wait(1)
        self.play(Create(graph),run_time = 2)
        self.wait(1)
        self.play(Create(graph_label))
        self.wait(1)

        a = 0.7
        b = 4.5
        a_label = MathTex("a").next_to(axes.coords_to_point(a, 0), DOWN).set_color(RED)
        b_label = MathTex("b").next_to(axes.coords_to_point(b, 0), DOWN).set_color(RED)
        self.play(Create(a_label), Create(b_label))
        f_a = func(a)
        f_b = func(b)
        dashline_fa = DashedLine(axes.coords_to_point(a, 0), axes.coords_to_point(a, f_a), color=ORANGE)
        dashline_fb = DashedLine(axes.coords_to_point(b, 0), axes.coords_to_point(b, f_b), color=ORANGE)
        self.play(Create(dashline_fa), run_time = 1)
        self.play(Create(dashline_fb), run_time = 1)
        self.wait(1)
        fa_label = MathTex("f(a)").next_to(axes.coords_to_point(a, f_a), LEFT).scale(0.7)
        fb_label = MathTex("f(b)").next_to(axes.coords_to_point(b, f_b), RIGHT).scale(0.7)
        self.play(Create(fa_label))
        self.play(Create(fb_label))
        self.wait(1)

        xa_fxa_dot, xb_fxb_dot, secant_line = draw_secant_line_at(0.7, 4.5)
        self.play(Create(xa_fxa_dot), Create(xb_fxb_dot))
        self.wait(1)
        self.play(Create(secant_line))
        self.wait(1)
        sekante_label = MathTex("Sekante").next_to(secant_line.get_center(), UP).scale(0.7)
        self.play(Create(sekante_label))
        self.wait(1)

        # Create a ValueTracker for the moving endpoint (starting at a)
        slope_tracker = ValueTracker(a)

        # Always redraw the moving tangent line from a to the current tracker value
        tangent_group = always_redraw(
            lambda: VGroup(*draw_tangent_line_at(slope_tracker.get_value()))
        )
        self.add(tangent_group)

        # Create an empty container for the fixed tangent line
        fixed_tangent_container = VGroup()
        self.add(fixed_tangent_container)
        
        def fixed_tangent_updater(mobject, dt):
            if slope_tracker.get_value() >= 1.4:
                tangent_1_4 = VGroup(*draw_tangent_line_at(1.4))
                tangent_1_4.tangent_fixed_point = 1.4  # mark with a custom attribute
                mobject.add(tangent_1_4)

            if slope_tracker.get_value() >= 3.6:
                tangent_3_6 = VGroup(*draw_tangent_line_at(3.6))
                tangent_3_6.tangent_fixed_point = 3.6  # mark with a custom attribute
                mobject.add(tangent_3_6)

        fixed_tangent_container.add_updater(fixed_tangent_updater)

        # Animate the moving tangent from a to b concurrently.
        self.play(slope_tracker.animate.set_value(b), run_time=10, rate_func=linear)
        self.remove(tangent_group)
        self.wait(1)





