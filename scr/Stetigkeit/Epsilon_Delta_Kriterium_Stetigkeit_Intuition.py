from manim import *

class EpsilonDeltaKriteriumStetigkeitIntuition(Scene):
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

        # Delta lines
        delta = 0.5
        x0_minus_delta = axes.coords_to_point(x0 - delta, 0)
        x0_plus_delta = axes.coords_to_point(x0 + delta, 0)
        delta_lines_to_x_axis = VGroup(
            DashedLine(x0_minus_delta, axes.coords_to_point(x0 - delta, func(x0 - delta)), color=YELLOW),
            DashedLine(x0_plus_delta, axes.coords_to_point(x0 + delta, func(x0 + delta)), color=YELLOW)
        )
        # Interval with delta under x-axis
        delta_interval = DoubleArrow(
            start=axes.coords_to_point(x0 - delta, -0.5),
            end=axes.coords_to_point(x0 + delta, -0.5),
            color=YELLOW
        )
        delta_label = MathTex("\\delta").next_to(delta_interval, DOWN)

        ###########################
        # Epsilon lines
        epsilon = 2
        # Interval with epsilon under y-axis
        fx0_minus_epsilon = axes.coords_to_point(0, fx0 - epsilon)
        fx0_plus_epsilon = axes.coords_to_point(0, fx0 + epsilon)
        epsilon_lines = VGroup(
            DashedLine(fx0_minus_epsilon, axes.coords_to_point(inverse_func(fx0 - epsilon), fx0 - epsilon), color=GOLD),
            DashedLine(fx0_plus_epsilon, axes.coords_to_point(inverse_func(fx0 + epsilon), fx0 + epsilon), color=GOLD)
        )
        # Interval with epsilon under y-axis
        epsilon_interval = DoubleArrow(
            start=axes.coords_to_point(0, fx0 - epsilon),
            end=axes.coords_to_point(0, fx0 + epsilon),
            color=GOLD
        )
        epsilon_label = MathTex("\\epsilon").next_to(epsilon_interval, RIGHT)

        ################################
        # 
        x0_minus_delta_fx_at_y_axis = axes.coords_to_point(0, func(x0 - delta))
        x0_plus_delta_fx_at_y_axis = axes.coords_to_point(0, func(x0 + delta))
        delta_lines_to_y_axis = VGroup(
            DashedLine(axes.coords_to_point(x0 - delta, func(x0 - delta)), x0_minus_delta_fx_at_y_axis, color=YELLOW),
            DashedLine(axes.coords_to_point(x0 + delta, func(x0 + delta)), x0_plus_delta_fx_at_y_axis, color=YELLOW)
        )


        ################################
         # Add all elements to the scene
        self.add(grid)  # Add the NumberPlane as the background
        self.play(Create(axes), Write(axes_labels))
        self.play(Create(graph_func))
        self.play(FadeIn(x0_dot))
        self.play(Create(dashed_to_x_axis), Create(dashed_to_y_axis))
        self.play(Write(x0_axis_label), Write(fx0_axis_label))
        self.wait(1)
        self.play(Create(delta_lines_to_x_axis,run_time=2))
        self.play(Create(delta_interval), Write(delta_label))
        self.wait(1)
        self.play(Create(epsilon_lines,run_time = 2))
        self.play(Create(epsilon_interval), Write(epsilon_label))
        self.wait(1)
        self.play(Create(delta_lines_to_y_axis,run_time = 2))
        self.wait(2)
        