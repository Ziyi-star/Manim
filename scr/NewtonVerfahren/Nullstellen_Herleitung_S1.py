from manim import *
from reactive_manim import *


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
        label_graph = axes.get_graph_label(
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
        label_xn = MathTex(r"\mathbf{x_n}", color=YELLOW).next_to(axes.c2p(xn, 0), DOWN).scale(0.6)
        label_fxn = MathTex("f(x_n)", color=WHITE).next_to(axes.c2p(0, func(xn)), RIGHT).scale(0.6)

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
        label_tangent = MathTex("T(x)", color=ORANGE).next_to(
            axes.c2p(3, func(xn) + slope * (3 - xn)),  # Position on tangent line
            DOWN,  # Label appears below the tangent line
        ).scale(0.6)

        # Add point and label for x_{n+1}
        x_n_plus_one = -2.4
        point_zero_approximate = Dot(axes.c2p(x_n_plus_one, 0), color=GREEN).scale(0.6)
        label_xn_zero_approximate = MathTex(r"\mathbf{x_{n+1}}", color=GREEN).next_to(axes.c2p(x_n_plus_one, 0), DOWN).scale(0.6)

        # ZERO POINT:
        point_zero = MathTex(r"\mathbf{x}", color=RED).scale(0.7).move_to(axes.c2p(-1.76, 0))

        # Beschriftung in Rectangle
        label_fxn_beschriftung = MathTex("f(x) = x^3 - 2x + 2", color=BLUE).scale(0.4).move_to(axes.c2p(-3, 20))
        label_tn_beschriftung = MathTex(
            r"T(x): \text{ Tangente bei } (x_n, f(x_n))", 
            color=ORANGE
        ).scale(0.4).next_to(label_fxn_beschriftung, DOWN, buff=0.1).align_to(label_fxn_beschriftung, LEFT)
        label_x_zero_beschriftung = MathTex(
            r"x_{n+1}: T(x_{n+1}) = 0", 
            color=GREEN
        ).scale(0.4).next_to(label_tn_beschriftung, DOWN, buff=0.1).align_to(label_fxn_beschriftung, LEFT)
        labels_group = VGroup(label_fxn_beschriftung, label_tn_beschriftung, label_x_zero_beschriftung)
        label_rect = SurroundingRectangle(labels_group, color=WHITE, buff=0.2)

        # Texts
        title = Tex("Newton Verfahren:", font_size=36).to_edge(LEFT * 1.5 + UP*1.5)

        # Create equations
        eq1 = MathTex(
            "T(x)", "=", "f(x_n)", "+", "f'(x_n)", "(x-", "x_n", ")",
            color=WHITE
        ).scale(0.6).next_to(title, DOWN, buff=0.5)

        eq1 = MathTex(
            "T(x)", "=", "f", "(", "x_n", ")", "+", "f'", "(", "x_n", ")", "(x-", "x_n", ")",
            color=WHITE
        ).scale(0.6).next_to(title, DOWN, buff=0.5)

        # Set all instances of x_n to yellow
        eq1[4].set_color(YELLOW)   # x_n in f(x_n)
        eq1[9].set_color(YELLOW)   # x_n in f'(x_n)
        eq1[12].set_color(YELLOW)  # x_n in (x-x_n)

        eq2 = MathTex(
            "T(", "x_{n+1}", ")", "=", "0",
            color=WHITE
        ).scale(0.6).next_to(eq1, DOWN, buff=0.5).align_to(eq1, LEFT)

        # Set x_{n+1} to green
        eq2[1].set_color(GREEN)


        # Add text and graph to the scene
        self.add(grid, title, axes)
        self.play(Create(graph), run_time=2)
        self.play(Write(label_graph), run_time=1.5)
        self.add(label_rect)
        self.play(Create(label_fxn_beschriftung), run_time=1.5)
        self.wait(1.5)

        # Add point and lines
        self.play(Create(point), run_time=1.5)
        self.wait(0.5)
        self.play(Create(vertical_line), run_time=1.5)
        self.play(Write(label_xn), run_time=1.5)
        self.wait(0.5)
        self.play(Create(horizontal_line), run_time=1.5)
        self.play(Write(label_fxn), run_time=1.5)
        self.wait(1.5)

        # Add tangent line and its label
        self.play(Create(tangent_line), run_time=2)
        self.play(Write(label_tangent), run_time=1.5)
        self.add(label_tn_beschriftung)
        self.wait(1.5)

        # Add approximate zero point
        self.play(Create(point_zero_approximate), run_time=1.5)
        self.play(Write(label_xn_zero_approximate), run_time=1.5)
        self.wait(1.5)
        self.add(label_x_zero_beschriftung)
        self.wait(1.5)
        self.play(Create(point_zero), run_time=1.5)
        self.wait(1.5)

        # Add equations with longer animations
        self.play(Write(eq1), run_time=3)
        self.wait(1.5)
        self.play(Write(eq2), run_time=3)
        self.wait(1.5)

        x_n = MathTex("x_n").set_color(YELLOW)
        f_x_n = MathTex("f(", x_n, ")")
        f_x_n_prime = MathTex("f'(", x_n, ")")
        x_n_plus_1 = MathTex("x_{n+1}").set_color(GREEN)
        eq3 = MathTex(
            [f_x_n, "+", [f_x_n_prime, "(", [x_n_plus_1, "-", x_n] , ")" ]],
            "=", 
            "0"
        ).scale(0.6).next_to(eq2, DOWN, buff=0.5).align_to(eq1, LEFT)
        self.play(Write(eq3), run_time=2)
        self.wait(2)



        eq3[0] = eq3[0][2]
        eq3[2] = MathTex( "-", f_x_n)

        anim = TransformInStages.progress(eq3, lag_ratio=0.4)
        anim.intercept(f_x_n).set_animation(lambda source, target: Transform(source, target, path_arc=PI/2))
        self.play(anim)
        self.wait(2)


        eq3[0] = eq3[0][2]
        eq3[2] = MathTex( "-", Fraction(eq3[2][1], f_x_n_prime))

        self.play(TransformInStages.progress(eq3, lag_ratio=0.4))
        self.wait(2)

        eq3[0] = eq3[0][0]
        eq3[2] = MathTex(eq3[2], "+", x_n)

        anim = TransformInStages.progress(eq3, lag_ratio=0.4)
        anim.intercept(x_n).set_animation(lambda source, target: Transform(source, target, path_arc=PI/2))
        self.play(anim)    
        self.wait(2)

        # Create rectangle around only the formula part
        rectangle_last = SurroundingRectangle(eq3, color=WHITE, buff=0.1)
        self.play(Create(rectangle_last), run_time=2)
        self.wait(2)