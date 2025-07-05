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


        # Animation
        self.add(grid)
        self.play(Create(axes))
        self.play(Create(eta_graph))
        self.play(Create(shaded_area))
        self.play(Create(h_line))
        self.wait(2)

