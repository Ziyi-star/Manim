from manim import *

# Define a global variable
GLOBAL_DELTA = 2

class EpsilonDeltaKriteriumStetigkeit(ZoomedScene):
    def construct(self):
        #Text
        Text_1 = Text("Epsilon-Delta-Kriterium in Stetigkeit", font_size=36, color=YELLOW).to_edge(UP, buff=2.5)
        Text_2 = Tex(r"$f$ hei\ss t stetig in $x_0$, wenn zu jedem $\varepsilon > 0$",).next_to(Text_1,DOWN)
        Text_3 = Tex(r"ein $\delta > 0$ existiert, so dass f\"ur alle $x \in D_f$ ",).next_to(Text_2,DOWN)
        Text_4 = Tex( r"mit $\lvert x - x_0\rvert < \delta$ gilt:",).next_to(Text_3,DOWN)
        Text_5 = Tex(r"$\lvert f(x) - f(x_0)\rvert < \varepsilon$.").next_to(Text_4,DOWN)

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
        def func_left(x):
            return np.sin(x)
                
         # Function graph
        graph_right = axes.plot(func_right, x_range=[0, 5], color=BLUE)
        graph_left = axes.plot(func_left, x_range=[-5, 0], color=BLUE)

        # x0 and f(x0)
        x0 = 2
        fx0 = func_right(x0)
        x0_fx0_dot = Dot(axes.coords_to_point(x0, fx0), color=RED)
        dashline_x0_fx0 = DashedLine(axes.c2p(x0, 0), x0_fx0_dot.get_center(), color=WHITE)
        # Labels for x0 dot
        x0_fx0_dot_label = MathTex("(x_0,f(x_0))", color = ORANGE).next_to(x0_fx0_dot, DOWN).scale(0.6)
        x0_dot = Dot(axes.coords_to_point(x0, 0), color=PURPLE_A)
        x0_dot_label = MathTex("x_0", color = PURPLE_A).next_to(x0_dot, UP).scale(0.6)

        # ValueTracker for epsilon
        epsilon_tracker = ValueTracker(1)
        #Function to create the dashed lines and background
        def get_epsilon_group():
            epsilon = epsilon_tracker.get_value()
            fx0_minus_epsilon = fx0 - epsilon
            fx0_plus_epsilon = fx0 + epsilon

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
            background_epsilon = Polygon(
                axes.c2p(-5, fx0_minus_epsilon),
                axes.c2p(5, fx0_minus_epsilon),
                axes.c2p(5, fx0_plus_epsilon),
                axes.c2p(-5, fx0_plus_epsilon),
                color=ORANGE,
                fill_opacity=0.2,
                stroke_width=0
            )
            return VGroup(background_epsilon, dashed_line_top, dashed_line_bottom)

        #delta = 2 , show me the function außerhalb der Schlauch
        delta_tracker = ValueTracker(2)
        def get_delta_group():
            delta = delta_tracker.get_value()
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
            return VGroup(background_delta, dashed_line_left, dashed_line_right)

    # Combined function for compute the highlighted points
        def combined_func(x):
            if x >= 0:
                return np.cos(x)
            else:
                return np.sin(x)
        
        def get_in_delta_but_not_in_epsilon():
            delta = delta_tracker.get_value()
            epsilon = epsilon_tracker.get_value()

            x_values = np.linspace(-5, 5, 1000)
            y_values = combined_func(x_values)

            in_purple_delta = (x_values >= x0 - delta) & (x_values <= x0 + delta)
            not_in_orange_epsilon = (y_values < fx0 - epsilon) | (y_values > fx0 + epsilon)
            highlight = in_purple_delta & not_in_orange_epsilon

            highlighted_points = VGroup()
            for x, y in zip(x_values[highlight], y_values[highlight]):
                point = Dot(axes.c2p(x, y), color=RED)
                highlighted_points.add(point)

            return highlighted_points

        # #Animations
        # self.play(Write(Text_1))
        # self.wait(1)
        # self.play(Write(Text_2))
        # self.wait(1)
        # self.play(Write(Text_3))
        # self.wait(1)
        # self.play(Write(Text_4))
        # self.wait(1)
        # self.play(Write(Text_5))
        # self.wait(1)
        # self.remove(Text_1,Text_2,Text_3,Text_4,Text_5)
        # self.wait(1)

        #Graph
        self.play(Create(grid))
        self.play(Create(axes))
        self.play(Create(graph_left))
        self.play(Create(graph_right))
        self.play(Create(x0_dot))
        self.play(Write(x0_dot_label))
        self.play(Create(dashline_x0_fx0))
        self.play(Create(x0_fx0_dot))
        self.play(Write(x0_fx0_dot_label))
        #self.wait(1)

        # #Situation 1
        # Always redraw the epsilon group
        math_text_1 = MathTex(r"\epsilon = 1", color = ORANGE)
        math_text_1.to_corner(UL)  # UR = Upper Right
        self.play(Write(math_text_1))
        #self.wait(2)

        epsilon_group = always_redraw(get_epsilon_group)
        self.add(epsilon_group)
        #self.wait(2)

        math_text_2 = MathTex(r"\delta = 2", color = PURPLE)
        math_text_2.next_to(math_text_1,DOWN)  
        # Show the math text with animation
        self.play(Write(math_text_2))
        #self.wait(2)
        delta_group = always_redraw(get_delta_group)
        self.add(delta_group)
        self.wait(2)

        # Situation 2: move epsilon math text from 1 to 0,7
        self.remove(math_text_1)
        math_text_epsilon = always_redraw(lambda: MathTex(r"\epsilon = {:.1f}".format(epsilon_tracker.get_value()),color = ORANGE).to_corner(UL))
        # Add the math text to the scene
        self.add(math_text_epsilon)
        self.play(epsilon_tracker.animate.set_value(0.7), run_time=4, rate_func=linear)
        #Graph pieces
        graph_piece2 = axes.plot(func_right, x_range=[0, 0.8], color=RED, stroke_width=6)
        graph_piece3 = axes.plot(func_right, x_range=[2.4, 3.6], color=RED, stroke_width=6)
        #Play the creation of the graph pieces simultaneously with a runtime of 2 seconds
        self.play(Create(graph_piece2))
        self.wait(1)
        self.play(Create(graph_piece3))
        self.wait(2)
        self.remove(graph_piece2,graph_piece3)
        #Animate the delta value
        graph_pieces = always_redraw(get_graph_pieces)
        self.add(graph_pieces)

        # #Move delta from 2 to 0.8
        # self.remove(math_text_2)
        # math_text_delta = always_redraw(lambda: MathTex(r"\delta = {:.1f}".format(delta_tracker.get_value()))
        #                                 .next_to(math_text_epsilon, DOWN))       
        # self.add(math_text_delta)
        # self.play(delta_tracker.animate.set_value(0.8), run_time=6, rate_func=linear)
        # self.wait(2)
        # #Zoom in, length and width here manually adjusted to look pretty
        # zoom_rect = Rectangle(
        #     width=2, height=2, color=YELLOW
        # ).move_to(x0_fx0_dot)
        # self.play(Create(zoom_rect))  # Animate the zoom rectangle
        # self.wait(1)
        #  # Scale the view to focus on the red point and DoubleArrow
        # self.play(self.camera.frame.animate.scale(0.5).move_to(x0_dot))  # Zoom in
        # self.wait(2)
        #  # Reset the camera to its original position
        # self.play(self.camera.frame.animate.scale(2).move_to(ORIGIN))  # Zoom out
        # self.wait(2)
