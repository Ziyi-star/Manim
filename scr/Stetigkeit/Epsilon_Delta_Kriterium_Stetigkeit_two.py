from manim import *

class EpsilonDeltaKriteriumStetigkeitTwo(ZoomedScene):
    def construct(self):
        #Text
        text1 = Text("Epsilon-Delta-Kriterium in Stetigkeit", font_size=36, color=YELLOW)

        text3 = MathTex(
             r"\forall \epsilon > 0, \exists \delta > 0, \text{ sodass, wenn }",
            font_size=32, color=WHITE
        ).next_to(text1, DOWN)
        text4 = MathTex(r"\forall x \in D_f:", font_size=32).next_to(text3, DOWN)
        math_expression = MathTex(
            r"|x - x_0| < \delta \implies |f(x) - f(x_0)| < \epsilon",
            font_size=36
        ).next_to(text4, DOWN)

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
        )

        # Axes setup
        axes = Axes(
            x_range=[-1, 5, 1],
            y_range=[0, 10, 1],
            axis_config={"include_numbers": False}
        ).add_coordinates()
        axes_labels = axes.get_axis_labels(x_label="x", y_label="f(x)")

        # Function definition
        def func(x):
            return x**2
        
        # Reversed function (swapping x and y)
        def inverse_func(y):
            return np.sqrt(y)

        
         # Function graph
        graph_func = axes.plot(func, color=GREEN)

         # x0 and f(x0)
        x0 = 2
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
        x0_axis_label = MathTex("x_0").next_to(axes.coords_to_point(x0, 0), DOWN)
        fx0_axis_label = MathTex("f(x_0)").next_to(axes.coords_to_point(0, fx0), LEFT)

         # little arrow around the point (x0, f(x0))
        little_arrow_at_point = DoubleArrow(
            start=axes.coords_to_point(x0, fx0+1),
            end=axes.coords_to_point(x0, fx0-1),
            color=RED
        )

        # Epsilon lines under y-axis
        epsilon = 2
        # Value relevant to (fx0 - epsilon) and (fx0 + epsilon)
        fx0_minus_epsilon =fx0 - epsilon
        fx0_plus_epsilon = fx0 + epsilon
        x0_minus_epsilon = inverse_func(fx0_minus_epsilon)
        x0_plus_epsilon = inverse_func(fx0_plus_epsilon)
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
        ###########################################
        # Zoom effect around the red point and DoubleArrow
        zoom_rect = SurroundingRectangle(
            x0_dot,  # The red point
            color=YELLOW,
            buff=1  # Padding around the point
        )
        self.play(Create(zoom_rect))  # Animate the zoom rectangle
        self.wait(1)

        # Scale the view to focus on the red point and DoubleArrow
        self.play(self.camera.frame.animate.scale(0.5).move_to(x0_dot))  # Zoom in
        self.wait(2)

        # Reset the camera to its original position
        self.play(self.camera.frame.animate.scale(2).move_to(ORIGIN))  # Zoom out
        self.wait(2)


        
        # Text
        # self.play(Write(text1))  # Animate writing the first text
        # self.wait(1)
        # self.play(Write(text3))
        # self.wait(1)
        # self.play(Write(text4))
        # self.wait(1)
        # self.play(Write(math_expression))
        # self.wait(1)
        # self.play(FadeOut(text1), FadeOut(text3), FadeOut(text4), FadeOut(math_expression))
        
        # # Graph
        self.add(grid)  # Add the NumberPlane as the background
        self.play(Create(axes), Write(axes_labels))
        self.play(Create(graph_func))
        self.play(FadeIn(x0_dot))
        self.play(Create(dashed_to_x_axis), Create(dashed_to_y_axis))
        self.play(Write(x0_axis_label), Write(fx0_axis_label))
        self.wait(1)
        self.play(Create(little_arrow_at_point, run_time=1))
        self.wait(1)
        self.play(Create(lines_from_y_axis_to_graph,run_time=1))
        self.wait(1)
        self.play(Create(lines_from_graph_to_x_axis, run_time=1))
        self.wait(2)


        # # Reset the camera to its original position
        # self.play(self.camera.frame.animate.scale(2).move_to(ORIGIN))  # Zoom out
        # self.wait(2)
        # self.play(FadeOut(zoom_circle), FadeOut(little_arrow_at_point))




       