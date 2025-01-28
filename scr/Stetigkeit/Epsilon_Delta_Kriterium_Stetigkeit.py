from manim import *

class EpsilonDeltaKriteriumStetigkeit(ZoomedScene):
    def construct(self):
        #Text
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
        #########################################
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
        ).add_coordinates()
       
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[0, 4, 1],
            axis_config={"include_numbers": False}
        ).add_coordinates()

        # Function definition
        def func_right(x):
            return np.cos(x)
        def inverse_func_right(x):
            return np.arccos(x)
                
         # Function graph
        graph_func = axes.plot(func_right, color=GREEN)

        # x0 and f(x0)
        x0 = 0
        fx0 = func(x0)

        x0_dot = Dot(axes.coords_to_point(x0, fx0), color=RED)

        # Dashed lines from (x0, f(x0)) to x,y axes
        dashed_to_x_axis = DashedLine(
            start=axes.coords_to_point(x0, fx0),
            end=axes.coords_to_point(x0, 0),
            color=BLUE
        )
        dashed_to_y_axis = DashedLine(
            start=axes.coords_to_point(x0, fx0),
            end=axes.coords_to_point(0, fx0),
            color=BLUE
        )

        # Labels for x0 on x-axis and f(x0) on y-axis
        x0_axis_label = MathTex("x_0", color = YELLOW).next_to(axes.coords_to_point(x0, 0), DOWN)
        fx0_axis_label = MathTex("f(x_0)", color = YELLOW).next_to(axes.coords_to_point(0, fx0), LEFT)

         # Epsilon lines under y-axis
        epsilon = 3
        # Value relevant to (fx0 - epsilon) and (fx0 + epsilon)
        fx0_minus_epsilon =fx0 - epsilon
        fx0_plus_epsilon = fx0 + epsilon
        x0_minus_epsilon = inverse_func(fx0_minus_epsilon)
        x0_plus_epsilon = inverse_func(fx0_plus_epsilon)

        delta = 0.65 #x0_plus_epsilon - x0
        #Points at y-axis
        fx0_minus_epsilon_point = axes.coords_to_point(0, fx0 - epsilon)
        fx0_plus_epsilon_point = axes.coords_to_point(0, fx0 + epsilon)
        #Points at x-axis
        x0_minus_epsilon_point = axes.coords_to_point(x0_minus_epsilon, 0)
        x0_plus_epsilon_point = axes.coords_to_point(x0_plus_epsilon, 0)
        #Point at Graph
        x0_fx0_minus_epsilon_point = axes.coords_to_point(x0_minus_epsilon, fx0_minus_epsilon)
        x0_fx0_plus_epsilon_point = axes.coords_to_point(x0_plus_epsilon, fx0_plus_epsilon)  

        #Draw lines
        lines_from_y_axis_to_graph = VGroup(
            DashedLine(fx0_minus_epsilon_point, x0_fx0_minus_epsilon_point, color=GOLD),
            DashedLine(fx0_plus_epsilon_point, x0_fx0_plus_epsilon_point, color=GOLD)
           
        )
        lines_from_graph_to_x_axis = VGroup(
            DashedLine(x0_fx0_minus_epsilon_point, x0_minus_epsilon_point, color=GOLD),
            DashedLine(x0_fx0_plus_epsilon_point, x0_plus_epsilon_point, color=GOLD)
        )

        #Arrows
        # Interval with epsilon under y-axis
        epsilon_interval = DoubleArrow(
            start=axes.coords_to_point(0, fx0 - epsilon),
            end=axes.coords_to_point(0, fx0 + epsilon),
            color=GOLD
        )
        epsilon_label = MathTex("2\\epsilon").next_to(epsilon_interval, RIGHT)
        # Interval with delta under x-axis
        delta_interval = DoubleArrow(
            start=axes.coords_to_point(x0 - delta, 0),
            end=axes.coords_to_point(x0 + delta, 0),
            color=YELLOW
        )
        delta_label = MathTex("2\\delta").next_to(delta_interval, UP) 


        #####################################
        # self.play(Write(text1)) 
        # self.wait(1)
        # self.play(Write(text2))
        # self.wait(1)
        # self.play(Write(text3))
        # self.wait(1)
        # self.play(Write(math_expression))
        # self.wait(1)
        # self.play(FadeOut(text1), FadeOut(text2), FadeOut(text3), FadeOut(math_expression))
        # self.wait(1)
        # self.play(Write(math_expression1))
        # self.wait(1)
        # self.play(FadeOut(math_expression1))
        # Graph
        self.add(grid)  # Add the NumberPlane as the background
        self.play(Create(axes))
        self.play(Create(graph_func))
        self.wait(1)
        self.play(FadeIn(x0_dot))
        self.play(Create(dashed_to_x_axis), Create(dashed_to_y_axis))
        self.play(Write(x0_axis_label), Write(fx0_axis_label))
        self.wait(1)
        self.play(Create(lines_from_y_axis_to_graph,run_time=1))
        self.wait(1)
        self.play(Create(lines_from_graph_to_x_axis, run_time=1))
        self.wait(1)
        self.play(Create(epsilon_interval), Write(epsilon_label))
        self.wait(1)
        self.play(Create(delta_interval), Write(delta_label))
        self.wait(1)
        # Zoom in, length and width here manually adjusted to look pretty
        zoom_rect = Rectangle(
            width=2.5, height=3.5, color=YELLOW
        ).move_to(axes.coords_to_point(x0, fx0))
        # Double arrow at Rectangles
        # Double arrow for width (delta)
        delta_arrow = DoubleArrow(
            start=zoom_rect.get_left(),
            end=zoom_rect.get_right(),
            color=BLUE
        )
        delta_label = MathTex("2\\delta").next_to(delta_arrow, DOWN)

        # Double arrow for height (epsilon)
        epsilon_arrow = DoubleArrow(
            start=zoom_rect.get_bottom(),
            end=zoom_rect.get_top(),
            color=GREEN
        )
        epsilon_label = MathTex("2\\epsilon").next_to(epsilon_arrow, RIGHT) 

        self.play(Create(zoom_rect))  # Animate the zoom rectangle
        self.wait(1)
        # Scale the view to focus on the red point and DoubleArrow
        self.play(self.camera.frame.animate.scale(0.5).move_to(x0_dot))  # Zoom in
        self.play(Create(delta_arrow), Write(delta_label))
        self.wait(2)
        self.play(Create(epsilon_arrow), Write(epsilon_label))
        self.wait(2)

        # Reset the camera to its original position
        self.play(self.camera.frame.animate.scale(2).move_to(ORIGIN))  # Zoom out
        self.wait(2)
