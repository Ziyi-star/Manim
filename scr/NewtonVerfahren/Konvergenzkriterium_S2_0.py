from manim import *

class KonvergenzkriteriumS2Zero(Scene):

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
        label_eta_graph = axes.get_graph_label(eta_graph, label='\\eta(x)', x_val=3, direction=UP)

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
        x0 = 0

        # Create a dot and label for x0
        x0_dot = Dot(
            axes.c2p(x0, 0),
            color=RED,
            radius=0.08
        )
        x0_label = MathTex(
            r"\mathbf{" + f"{x0:.2f}" + "}",
            color=RED
        ).scale(0.6).next_to(axes.c2p(x0, 0), DOWN, buff=0.6)
        x0_arrow = Arrow(
            end=x0_dot.get_center(),
            start=x0_label.get_top(),
            color=RED,
            buff=0.1,
            max_tip_length_to_length_ratio=0.15
        )

        #labels
        convergence_label = MathTex(
            r"\eta(x) < 1:", r"\text{ Newton Verfahren}", r"\\\text{ konvergiert lokal}",
            color=GREEN
        ).scale(0.6).to_edge(LEFT + UP * 2)
        divergence_label = MathTex(
            r"\eta(x) \geq 1:", r"\text{ Newton Verfahren}", r"\\\text{ divergiert}",
            color=RED
        ).scale(0.6).next_to(convergence_label, DOWN, aligned_edge=LEFT)


        # Add all elements without animation
        self.add(
            grid,
            axes,
            eta_graph,
            label_eta_graph,
            h_line,
            shaded_area,
            x_axis_green_highlights,
            x_axis_red_highlights,
            x_dots,
            x_labels,
            convergence_label,
            divergence_label
        )

        # Highlight x0 point
        self.play(Create(x0_dot), run_time=1)
        self.play(Create(x0_arrow), run_time=1)
        self.play(Write(x0_label), run_time=1)
        self.wait(2)

        
