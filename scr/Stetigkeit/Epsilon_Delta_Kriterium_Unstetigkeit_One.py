from manim import *

class EpsilonDeltaKriteriumUnstetigkeitOne(Scene):
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

        # Axes
        axes = Axes(
            x_range=[-1, 4, 1],
            y_range=[-1, 4, 1],
            axis_config={"include_tip": True, "include_numbers": True},
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="f(x)")

        def func_below(x):
            return 0.5 * (x**2)
        def inverse_func_below(y):
            return np.sqrt(2 * y)

        def func_above(x):
            return 0.5 * (x**2) + 1
        def inverse_func_above(y):
            return np.sqrt(2 * (y-1))
        
        graph_1 = axes.plot(func_below, x_range=[-0.5, 1.5], color=GREEN)
        graph_2 = axes.plot(func_above, x_range=[1.5, 3], color=GREEN)


        # Add open circle at a specific point (x0, f(x0))
        x0 = 1.5
        y0_func_below =func_below(x0)
        y0_func_above = func_above(x0)

        # Add a Dot at (x0, f(x0))
        dot_below = Dot(axes.coords_to_point(x0, y0_func_below), color=RED)
        
       # Dashed lines from (x0, f(x0)) to x,y axes
        dashed_to_x_axis = DashedLine(
            start=axes.coords_to_point(x0, y0_func_below),
            end=axes.coords_to_point(x0, 0),
            color=BLUE
        )
        dashed_to_y_axis = DashedLine(
            start=axes.coords_to_point(x0, y0_func_below),
            end=axes.coords_to_point(0, y0_func_below),
            color=BLUE
        )
        # Labels for x0 on x-axis and f(x0) on y-axis
        x0_axis_label = MathTex("x_0").next_to(axes.coords_to_point(x0, 0), DOWN)
        fx0_axis_label = MathTex("f(x_0)").next_to(axes.coords_to_point(0, y0_func_below), LEFT)

        #Circle at func_above(x0)
        circle_position = axes.coords_to_point(x0, y0_func_above)
        circle_above = Circle(radius=0.1, color=RED).move_to(circle_position)

        #Epsilon lines
        epsilon = 0.7
        y0_func_below_minus_epsilon = y0_func_below - epsilon
        y0_func_below_plus_epsilon = y0_func_below + epsilon
        x0_func_below_minus_epsilon_graph_below = inverse_func_below(y0_func_below_minus_epsilon)
        #Points at y-axis
        y0_func_below_minus_epsilon_point = axes.coords_to_point(0, y0_func_below_minus_epsilon)
        y0_func_below_plus_epsilon_point = axes.coords_to_point(0, y0_func_below_plus_epsilon)
        #Draw dashed lines for epsilon
        line_from_y_axis_to_graph = VGroup(
            DashedLine(y0_func_below_minus_epsilon_point, axes.coords_to_point(3,y0_func_below_minus_epsilon), color=GOLD),
            DashedLine(y0_func_below_plus_epsilon_point, axes.coords_to_point(3, y0_func_below_plus_epsilon), color=GOLD)
        )
        #Double Arrow with epsilon
        epsilon_interval = DoubleArrow(
            start=y0_func_below_minus_epsilon_point,
            end=y0_func_below_plus_epsilon_point,
            color=YELLOW
        )
        epsilon_label = MathTex("2\\epsilon", color= YELLOW).next_to(epsilon_interval, RIGHT)

        # delta lines
        delta = 0.5
        x0_minus_delta = x0 - delta
        x0_plus_delta = x0 + delta
        y0_func_below_minus_delta = func_below(x0_minus_delta)
        y0_func_above_plus_delta = func_above(x0_plus_delta)
        #Points at x-axis
        x0_minus_delta_x_axis_point = axes.coords_to_point(x0_minus_delta, 0)
        x0_plus_delta_x_axis_point = axes.coords_to_point(x0_plus_delta, 0)
        #Points at the Graph
        x0_minus_delta_graph_below = axes.coords_to_point(x0_minus_delta, y0_func_below_minus_delta)
        x0_plus_delta_graph_above = axes.coords_to_point(x0_plus_delta, y0_func_above_plus_delta)
        # Line from x axis to Graph
        line_from_x_axis_to_graph = VGroup(
            DashedLine(x0_minus_delta_x_axis_point, x0_minus_delta_graph_below, color=YELLOW),
            DashedLine(x0_plus_delta_x_axis_point, x0_plus_delta_graph_above, color=YELLOW)
        )
        #Upper point in y axis projection
        y0_func_above_plus_delta_point = axes.coords_to_point(0, y0_func_above_plus_delta)
        line_from_graph_to_y_axis_above = DashedLine(x0_plus_delta_graph_above, y0_func_above_plus_delta_point, color=YELLOW)
        #Double Arrow with delta
        delta_interval = DoubleArrow(
            start=x0_minus_delta_x_axis_point,
            end=x0_plus_delta_x_axis_point,
            color=YELLOW
        )
        delta_label = MathTex("2\\delta", color=YELLOW ).next_to(delta_interval, DOWN)

        # Display everything
        self.add(grid)
        self.play(Create(axes), Write(axes_labels))
        self.wait(1)
        self.play(Create(graph_1,run_time = 1))
        self.wait(1)
        self.play(Create(graph_2,run_time = 1)) 
        self.wait(1)
        self.play(Create(dot_below), Create(dashed_to_x_axis,run_time =1),Create(dashed_to_y_axis,run_time =1))
        self.play(Write(x0_axis_label), Write(fx0_axis_label))
        self.wait(1) 
        self.play(Create(circle_above))
        self.wait(1)
        self.play(Create(line_from_y_axis_to_graph))
        self.wait(1)
        self.play(Create(epsilon_interval), Write(epsilon_label))
        self.wait(1)
        self.play(Create(line_from_x_axis_to_graph))
        self.wait(1)
        self.play(Create(line_from_graph_to_y_axis_above))
        self.wait(1)
        self.play(Create(delta_interval), Write(delta_label))
        self.wait(1)



       