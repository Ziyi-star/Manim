from manim import *

class KonvergenzkriteriumS2(Scene):

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
            axis_config={"include_numbers": True},
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
            MathTex(f"{x:.2f}", color=WHITE)
            .scale(0.6)
            .next_to(axes.c2p(x, 0), DOWN, buff=0.2)
            for x in x_points
        ])

        #labels
        convergence_label = MathTex(
            r"\eta(x) < 1:", r"\text{ Newton Verfahren}", r"\\\text{ konvergiert lokal}",
            color=GREEN
        ).scale(0.6).to_edge(LEFT + UP * 2)
        divergence_label = MathTex(
            r"\eta(x) \geq 1:", r"\text{ Newton Verfahren}", r"\\\text{ divergiert}",
            color=RED
        ).scale(0.6).next_to(convergence_label, DOWN, aligned_edge=LEFT)


        # Animation
        self.add(grid)
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
        self.play(Write(convergence_label), run_time=2)
        self.play(Write(divergence_label), run_time=2)
        self.wait(2)
