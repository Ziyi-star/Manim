from manim import *

class KonvergenzkriteriumS2MinusTwoFive(Scene):

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


        # Define base functions
        def func(x):
            return x**3 - 2*x + 2

        def func_prime(x):
            return 3*x**2 - 2

        def func_double_prime(x):
            return 6*x

        def eta(x):
            try:
                fp = func_prime(x)
                if abs(fp) < 1e-3:
                    return 5  # Cap it to avoid spikes (or return 0 to ignore)
                return abs((func(x) * func_double_prime(x)) / (fp**2))
            except:
                return 5

        # Axes setup
        axes = Axes(
            x_range=[-3.5, 3.5, 1],
            y_range=[0, 4.5, 0.5],
            x_length=12,
            y_length=6,
            axis_config={"include_numbers": True, "font_size": 24},
            tips=True,
        ).shift(UP*0.5 + RIGHT*1)
 
        # Plot η(x)
        eta_graph = axes.plot(
            eta,
            x_range=[-3, 3],
            color=BLUE,
            use_smoothing=False,
        )
        label_eta_graph = axes.get_graph_label(eta_graph, label='\\eta(x)', x_val=1.2, direction=RIGHT)

        # Define shaded region: η(x) < 1
        def eta_clipped(x):
            try:
                val = eta(x)
                return val if val < 1 else 0
            except:
                return 0

        # Get shaded graph object
        shaded_graph = axes.plot(
            eta_clipped,
            x_range=[-3, 3],
            color=GREEN,
        )
 

        # Generate shaded rectangles under shaded_graph
        shaded_area = axes.get_riemann_rectangles(
            shaded_graph,
            x_range=[-3, 3],
            dx=0.01,
            input_sample_type="center",
            stroke_width=0,
            fill_opacity=0.4,
            color=GREEN
        )

        # Add horizontal line at y=1
        h_line = DashedLine(
            start=axes.c2p(-3, 1),  # Start at x=-3, y=1
            end=axes.c2p(3, 1),     # End at x=3, y=1
            color=RED,
        )

        # Create green line segments on x-axis for regions where η(x) < 1
        x_values = np.linspace(-3, 3, 1000)
        green_intervals = [(x1, x2) for x1, x2 in zip(x_values[:-1], x_values[1:]) 
                    if eta(x1) < 1 and eta(x2) < 1]
        red_intervals = [(x1, x2) for x1, x2 in zip(x_values[:-1], x_values[1:]) 
                if eta(x1) >= 1 and eta(x2) >= 1]

        x_axis_green_highlights = VGroup(*[
            Line(
                start=axes.c2p(interval[0], 0),
                end=axes.c2p(interval[1], 0),
                color=GREEN,
                stroke_width=5
            )
            for interval in green_intervals
        ])

        x_axis_red_highlights = VGroup(*[
            Line(
                start=axes.c2p(interval[0], 0),
                end=axes.c2p(interval[1], 0),
                color=RED,
                stroke_width=5
            )
            for interval in red_intervals
        ])

        # Create labels for specific x-values
        x_points = [-1.44, -0.22, 0.32, 1.47]
        x_dots = VGroup(*[
            Dot(
                axes.c2p(x, 0),
                color=YELLOW,
                radius=0.05
            )
            for x in x_points
        ])
        x_labels = VGroup(*[
            MathTex(r"\mathbf{" + f"{x:.2f}" + "}", color=YELLOW)  # Add \mathbf for bold text
            .scale(0.6)
            .next_to(axes.c2p(x, 0), DOWN, buff=0.2)
            for x in x_points
        ])

        # Highlight specific point: x0 = -2.5
        x0 = -2.5

        # Create a dot and label for x0
        x0_dot = Dot(
            axes.c2p(x0, 0),
            color=GREEN,
            radius=0.08
        )
        x0_label = MathTex(
            r"\mathbf{" + f"{x0:.2f}" + "}",
            color=GREEN
        ).scale(0.6).next_to(axes.c2p(x0, 0), DOWN, buff=0.6)
        x0_arrow = Arrow(
            end=x0_dot.get_center(),
            start=x0_label.get_top(),
            color=GREEN,
            buff=0.1,
            max_tip_length_to_length_ratio=0.15
        )

        # Labels
        titel_1 = MathTex(
            r"\text{Konvergenzindikator:}", 
            ).scale(0.8).to_edge(LEFT + UP * 2)
        titel_2 = MathTex(
            r"\eta(x)", r"=", r"\left|\frac{f(x) \cdot f''(x)}{(f'(x))^2}\right|"
        ).scale(0.8).next_to(titel_1, DOWN, buff=0.5)

        convergence_label = MathTex(
            r"\\\text{Konvergenzbedingung: }",r"\eta(x) < 1", 
            color=GREEN
        ).scale(0.6).next_to(titel_2, DOWN, buff=0.5)


        # Animation
        self.add(grid, titel_1, titel_2, convergence_label)
        self.play(Create(axes))
        self.play(Create(eta_graph), run_time=2)
        self.play(Write(label_eta_graph), run_time=1)
        self.play(Create(h_line), run_time=2)
        self.play(Create(shaded_area), run_time=2)
        self.play(Create(x_axis_green_highlights), run_time=2)
        self.play(Create(x_axis_red_highlights), run_time=2)
        self.play(
            Create(x_dots),
            Write(x_labels),
            run_time=2
        )
        #self.wait(2)

        # Highlight x0 point
        self.play(Create(x0_dot), run_time=1)
        self.play(Create(x0_arrow), run_time=1)
        self.play(Write(x0_label), run_time=1)
        self.wait(2)

        
