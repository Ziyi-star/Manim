from manim import *

# Define a global variable
GLOBAL_DELTA = 2

class EpsilonDeltaKriteriumStetigkeit(ZoomedScene):
    def construct(self):
        #Text

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
        graph_right = axes.plot(func_right, x_range=[0, 5], color=BLUE)
        graph_left = axes.plot(func_left, x_range=[-5, 0], color=BLUE)

        # x0 and f(x0)
        x0 = TAU/4
        fx0 = func_right(x0)
        x0_fx0_dot = Dot(axes.coords_to_point(x0, fx0), color=RED)
        # Labels for x0 dot
        x0_fx0_dot_label = MathTex("(x_0,f(x_0))", color = ORANGE).next_to(x0_fx0_dot, UP).scale(0.6)
        x0_dot = Dot(axes.coords_to_point(x0, 0), color=PURPLE_A)
        x0_dot_label = MathTex("x_0", color = PURPLE_A).next_to(x0_dot, DOWN).scale(0.6)

        # ValueTracker for epsilon
        epsilon_tracker = ValueTracker(1)
        # Epsilon lines under y-axis
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

        # Function to create the graph pieces, here left_range, middle_range variate to have changeable graphs
        def get_graph_pieces():
            delta = delta_tracker.get_value()
            delta_change = GLOBAL_DELTA - delta
            left_range = -0.4 + delta_change
            middle_range = 0 + delta_change - 0.4
            if (left_range < 0):
                graph_piece1 = axes.plot(func_left, x_range=[-0.4+delta_change, 0], color=RED, stroke_width=6)
                graph_piece2 = axes.plot(func_right, x_range=[0, 0.8], color=RED, stroke_width=6)
                graph_piece3 = axes.plot(func_right, x_range=[2.4, 3.6-delta_change], color=RED, stroke_width=6)
            if (left_range > 0):
                graph_piece1 = axes.plot(func_left, x_range=[0, 0], color=GREEN, stroke_width=6)
                graph_piece2 = axes.plot(func_right, x_range=[middle_range, 0.8], color=RED, stroke_width=6)
                graph_piece3 = axes.plot(func_right, x_range=[2.4, 3.6-delta_change], color=RED, stroke_width=6)
            return VGroup(graph_piece1, graph_piece2, graph_piece3)

        #Animations
        self.play(Create(grid))
        self.play(Create(axes))
        self.play(Create(graph_left))
        self.play(Create(graph_right))
        self.play(Create(x0_dot))
        self.play(Write(x0_dot_label))
        self.play(Create(x0_fx0_dot))
        self.play(Write(x0_fx0_dot_label))
        self.wait(1)
        # Always redraw the epsilon group
        epsilon_group = always_redraw(get_epsilon_group)
        self.add(epsilon_group)
        self.wait(2)
        delta_group = always_redraw(get_delta_group)
        self.add(delta_group)
        self.wait(1)
         # Animate the epsilon value
        self.play(epsilon_tracker.animate.set_value(0.7), run_time=4, rate_func=linear)
        # Graph pieces
        graph_piece1 = axes.plot(func_left, x_range=[-0.4, 0], color=RED, stroke_width=6)
        graph_piece2 = axes.plot(func_right, x_range=[0, 0.8], color=RED, stroke_width=6)
        graph_piece3 = axes.plot(func_right, x_range=[2.4, 3.6], color=RED, stroke_width=6)
        # Play the creation of the graph pieces simultaneously with a runtime of 2 seconds
        self.play(Create(graph_piece1))
        #self.wait(1)
        self.play(Create(graph_piece2))
        #self.wait(1)
        self.play(Create(graph_piece3))
        #self.wait(2)
        self.remove(graph_piece1,graph_piece2,graph_piece3)
        # Animate the delta value
        graph_pieces = always_redraw(get_graph_pieces)
        self.add(graph_pieces)
        self.play(delta_tracker.animate.set_value(0.8), run_time=6, rate_func=linear)
        self.wait(2)
        #Zoom in, length and width here manually adjusted to look pretty
        zoom_rect = Rectangle(
            width=2, height=2, color=YELLOW
        ).move_to(x0_fx0_dot)
        self.play(Create(zoom_rect))  # Animate the zoom rectangle
        self.wait(1)
         # Scale the view to focus on the red point and DoubleArrow
        self.play(self.camera.frame.animate.scale(0.5).move_to(x0_dot))  # Zoom in
        self.wait(2)
         # Reset the camera to its original position
        self.play(self.camera.frame.animate.scale(2).move_to(ORIGIN))  # Zoom out
        self.wait(2)
