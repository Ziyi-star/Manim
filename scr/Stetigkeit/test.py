from manim import *

class Test(Scene):
    def construct(self):
        text1 = Text("Epsilon-Delta-Kriterium in Stetigkeit", font_size=36, color=YELLOW)
        text2 = MathTex(
             r"\forall \epsilon > 0, \exists \delta > 0, \text{ sodass, wenn }",
            font_size=32, color=WHITE
        ).next_to(text1, DOWN)
        text3 = MathTex(r"\forall x \in D_f:", font_size=32).next_to(text2, DOWN)
        math_expression = MathTex(
            r"|x - x_0| < \delta \implies |f(x) - f(x_0)| < \epsilon",
            font_size=36
        ).next_to(text3, DOWN)

        math_expression1 = MathTex(r"f(x) = x^2", font_size=48, color=WHITE)
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
       
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-2, 2, 1],
            axis_config={"include_numbers": False}
        ).add_coordinates()

        # Function definition
        def func_right(x):
            return np.cos(x)
        def inverse_func_right(x):
            return np.arccos(x)
        def func_left(x):
            return np.sin(x)
                
         # Function graph
        graph_right = axes.plot(func_right, x_range=[0, 5], color=GREEN)
        graph_left = axes.plot(func_left, x_range=[-5, 0], color=GREEN)

        # x0 and f(x0)
        x0 = TAU/4
        fx0 = func_right(x0)
        x0_fx0_dot = Dot(axes.coords_to_point(x0, fx0), color=RED)
        # Labels for x0 dot
        x0_fx0_dot_label = MathTex("(x_0,f(x_0))", color = ORANGE).next_to(x0_fx0_dot, UP).scale(0.6)
        x0_dot = Dot(axes.coords_to_point(x0, 0), color=PURPLE_A)
        x0_dot_label = MathTex("x_0", color = PURPLE_A).next_to(x0_dot, DOWN).scale(0.6)

        # # Epsilon lines under y-axis

        
        epsilon = 1
        # Value relevant to (fx0 - epsilon) and (fx0 + epsilon)
        fx0_minus_epsilon =fx0 - epsilon
        fx0_plus_epsilon = fx0 + epsilon

        # orange Schlauch with lines transparent background color
        dashed_line_top = DashedLine(
            start=axes.c2p(-5, fx0_plus_epsilon),
            end=axes.c2p(5, fx0_plus_epsilon),
            color=ORANGE
        )
        dashed_line_bottom = DashedLine(
            start=axes.c2p(-5, fx0_minus_epsilon),
            end=axes.c2p(5, fx0_minus_epsilon),
            color=ORANGE
        )
        # Create the background color
        background_epsilon = Polygon(
            axes.c2p(-5, fx0_minus_epsilon),
            axes.c2p(5, fx0_minus_epsilon),
            axes.c2p(5, fx0_plus_epsilon),
            axes.c2p(-5, fx0_plus_epsilon),
            color=ORANGE,
            fill_opacity=0.2,
            stroke_width=0
        )

        #todo: delta = 2 , show me the function außerhalb der Schlauch
        delta = 2
        x0_minus_delta = x0 - delta
        x0_plus_delta = x0 + delta
        # Create the dashed lines for delta
        dashed_line_left = DashedLine(
            start=axes.c2p(x0_minus_delta, -2),
            end=axes.c2p(x0_minus_delta, 2),
            color=PURPLE
        )
        dashed_line_right = DashedLine(
            start=axes.c2p(x0_plus_delta, -2),
            end=axes.c2p(x0_plus_delta, 2),
            color=PURPLE
        )

        # Create the background color for delta
        background_delta = Polygon(
            axes.c2p(x0_minus_delta, -2),
            axes.c2p(x0_plus_delta, -2),
            axes.c2p(x0_plus_delta, 2),
            axes.c2p(x0_minus_delta, 2),
            color=PURPLE,
            fill_opacity=0.2,
            stroke_width=0
        )
        # todo: delta move from 2 to 1, show me the function außerhalb der Schlauch with always redraw

        #todo:zoom: at end all functions are in Schlauch


        self.play(Create(grid))
        self.play(Create(axes))
        self.play(Create(graph_left))
        self.play(Create(graph_right))
        self.play(Create(x0_dot))
        self.play(Write(x0_dot_label))
        self.play(Create(x0_fx0_dot))
        self.play(Write(x0_fx0_dot_label))
        self.play(Create(dashed_line_bottom), Create(dashed_line_top))
        self.play(Create(background_epsilon))
        self.add(background_delta, dashed_line_left, dashed_line_right)

        self.wait(2)


