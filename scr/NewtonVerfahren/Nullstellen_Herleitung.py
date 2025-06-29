from manim import *

class NullstellenHerleitung(Scene):
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

        # Funktion Animation
        # Create axes for the graph on the right
        axes = Axes(
            x_range=[-3.5, 3.5, 1],
            y_range=[-23, 23, 5],
            y_length=10,
            x_length=12,
            axis_config={"include_numbers": True, "font_size": 24}
        ).scale(0.75).to_edge(LEFT, buff=5)

        # Define a function for the graph
        def func(x):
            return x**3 - 2*x + 2

        # Plot the function
        graph = axes.plot(func, x_range=[-3, 3], color=BLUE)
        graph_label = axes.get_graph_label(
            graph, 
            label="f(x)", 
            x_val=3.2,  # Position where label appears
            direction=LEFT * 1.5,
            color=BLUE
        ).scale(0.6)

        # Add point at xn = -1
        xn = -1.2
        point = Dot(axes.c2p(xn, func(xn)), color=YELLOW).scale(0.6)
        
        # Create dashed lines
        vertical_line = DashedLine(
            start=axes.c2p(xn, func(xn)),
            end=axes.c2p(xn, 0),
            color=WHITE,
        )

        horizontal_line = DashedLine(
            start=axes.c2p(xn, func(xn)),
            end=axes.c2p(0, func(xn)),
            color=WHITE,
        )
        
        # Add labels
        xn_label = MathTex(r"\mathbf{x_n}", color=YELLOW).next_to(axes.c2p(xn, 0), DOWN).scale(0.6)
        fxn_label = MathTex("f(x_n)", color=WHITE).next_to(axes.c2p(0, func(xn)), RIGHT).scale(0.6)

        # Define derivative function
        def func_derivative(x):
            return 3*x**2 - 2

        # Calculate slope at xn
        slope = func_derivative(xn)
        
        # Calculate points for tangent line
        x1 = -3
        x2 = 3
        y1 = func(xn) + slope * (x1 - xn)
        y2 = func(xn) + slope * (x2 - xn)

        # Create tangent line
        tangent_line = DashedLine(
            start=axes.c2p(x1, y1),
            end=axes.c2p(x2, y2),
            color=ORANGE
        )
        tangent_label = MathTex("T(x)", color=ORANGE).next_to(
            axes.c2p(3, func(xn) + slope * (3 - xn)),  # Position on tangent line
            UP,  # Label appears above the tangent line
        ).scale(0.6)

        # Add point and label for x_{n+1}
        xn_next = -2.4
        point_zero = Dot(axes.c2p(xn_next, 0), color=RED).scale(0.6)

        xn_zero_label = MathTex(r"\mathbf{x_{n+1}}", color=RED).next_to(axes.c2p(xn_next, 0), DOWN).scale(0.6)


        # Texts
        title = Tex("Newton Verfahren:", font_size=36).to_edge(LEFT * 1.5 + UP*1.5)
        # Create equations
        eq1 = MathTex(
            "T(x)", "=", "f(x_n)", "+", "f'(x_n)", "(x-x_n)",
            color=WHITE
        ).scale(0.6).next_to(title, DOWN, buff=0.5)

        eq2 = MathTex(
            "T(x)", "=", "0",
            color=WHITE
        ).scale(0.6).next_to(eq1, DOWN,buff=0.5)

        eq3 = MathTex(
            "f(x_n)", "+", "f'(x_n)", "(x-x_n)", "=", "0",
            color=WHITE
        ).scale(0.6).next_to(eq2, DOWN,buff=0.5)

        eq4 = MathTex(
            "x", "-", "x_n", "=",  "-", "\\frac{f(x_n)}{f'(x_n)}",
            color=WHITE
        ).scale(0.6).next_to(eq3, DOWN,buff=0.5)

        eq5 = MathTex(
            "x", "=", "x_{n+1}",
            color=WHITE
        ).scale(0.6).next_to(eq4, DOWN,buff=0.5)

        eq6 = MathTex(
            "x_{n+1}", "=", "x_n", "-", "\\frac{f(x_n)}{f'(x_n)}",
            color=WHITE
        ).scale(0.6).next_to(eq5, DOWN,buff=0.5)

        # Add text and graph to the scene
        self.add(grid, title, axes)
        self.play(Create(graph), run_time=1)
        self.play(Write(graph_label), run_time=1)
        self.wait(1)
        self.play(Create(point), run_time=1)
        self.play(Create(vertical_line), run_time=1)
        self.play(Write(xn_label), run_time=1)
        self.play(Create(horizontal_line), run_time=1)
        self.play(Write(fxn_label), run_time=1)
        self.wait(1)
        self.play(Create(tangent_line), run_time=1)
        self.play(Write(tangent_label), run_time=1)
        self.wait(1)
        self.play(Create(point_zero), run_time=1)
        self.play(Write(xn_zero_label), run_time=1)
        self.wait(1)

        # Add equations to the scene
        self.play(Write(eq1), run_time=2)
        self.play(Write(eq2), run_time=2)
        self.play(Write(eq3), run_time=2)
        self.play(Write(eq4), run_time=2)
        self.play(Write(eq5), run_time=2)
        self.play(Write(eq6), run_time=2)
        self.wait(2)
