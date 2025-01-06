from manim import *

class EpsilonDeltaKriteriumStetigkeitTwo(ZoomedScene):
    def construct(self):
        #Text
        text1 = Text("Aber was bedeutet das in Konkret:", font_size=36, color=YELLOW)

        text2 = MathTex(
             r"\forall \epsilon > 0, \exists \delta > 0: ",
            font_size=36, color=WHITE
        ).next_to(text1, DOWN,buff=0.5)

        # self.play(Write(text1))
        # self.wait(1)
        # self.play(Write(text2))
        # self.wait(1)
        # self.play(FadeOut(text1), FadeOut(text2))
        # self.wait(1)

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
            x_range=[-1, 5, 0.5],
            y_range=[0, 10, 1],
            axis_config={"include_numbers": False}
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="f(x)")

        # Function definition
        def func(x):
            return 0.5 * x**2 + 0.5
        
        # Reversed function (swapping x and y)
        def inverse_func(y):
            return np.sqrt(2 * (y - 0.5))

        
         # Function graph
        graph_func = axes.plot(func, color=GREEN)

         # x0 and f(x0)
        x0 = 3
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
        epsilon = 0.05
        # Interval with epsilon under y-axis
        fx0_minus_epsilon = axes.coords_to_point(0, fx0 - epsilon)
        fx0_plus_epsilon = axes.coords_to_point(0, fx0 + epsilon)
        epsilon_lines_to_y_axis = VGroup(
            DashedLine(fx0_minus_epsilon, axes.coords_to_point(inverse_func(fx0 - epsilon), fx0 - epsilon), color=GOLD),
            DashedLine(fx0_plus_epsilon, axes.coords_to_point(inverse_func(fx0 + epsilon), fx0 + epsilon), color=GOLD)
        )
        # todo: delta range ??
        delta_lines_to_x_axis = VGroup(
            DashedLine(fx0_minus_epsilon, axes.coords_to_point(inverse_func(fx0 - epsilon), fx0 - epsilon), color=GOLD),
            DashedLine(fx0_plus_epsilon, axes.coords_to_point(inverse_func(fx0 + epsilon), fx0 + epsilon), color=GOLD)
        )

        self.add(grid)  # Add the NumberPlane as the background
        self.play(Create(axes), Write(axes_labels))
        self.play(Create(graph_func))
        self.play(FadeIn(x0_dot))
        self.play(Create(dashed_to_x_axis), Create(dashed_to_y_axis))
        self.play(Write(x0_axis_label), Write(fx0_axis_label))
        self.wait(1)
        self.play(Create(little_arrow_at_point, run_time=1))
        self.wait(1)
        self.play(Create(epsilon_lines))
        self.wait(2)


        # Zoom effect around the red point and DoubleArrow
        zoom_circle = Circle(
            radius=1, 
            color=YELLOW,  
            stroke_width=1,  
        ).move_to(x0_dot)


        # self.play(Create(zoom_circle))  # Animate the zoom rectangle
        # self.wait(1)
        # # Scale the view to focus on the red point and DoubleArrow
        # self.play(self.camera.frame.animate.scale(0.5).move_to(x0_dot))  # Zoom in
        # self.wait(2)
        ###########################################
        #play

       

        # # Reset the camera to its original position
        # self.play(self.camera.frame.animate.scale(2).move_to(ORIGIN))  # Zoom out
        # self.wait(2)
        # self.play(FadeOut(zoom_circle), FadeOut(little_arrow_at_point))




       