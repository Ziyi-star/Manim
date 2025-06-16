from manim import *

class TaylorpolynomeT1(ZoomedScene):
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
       
        axes = Axes(
            x_range=[-2.0, 2.5, 0.5],
            y_range=[0, 8, 1],
            axis_config={"include_numbers": True}
        ).add_coordinates()

        def exp_func(x):
            return np.exp(x)
        
        point = Dot(axes.c2p(0, exp_func(0)), color=YELLOW)
        graph_exp = axes.plot(exp_func, color=BLUE, x_range=[-2.0, 2.0])
        label_exp = axes.get_graph_label(graph_exp, label='e^x', direction=UP)
        
        # # Create graphs for left and right portions
        # left_graph = axes.plot(
        #     exp_func,
        #     x_range=[-2.0,-0.01],
        #     color=BLUE
        # ).reverse_points()
        # right_graph = axes.plot(
        #     exp_func,
        #     x_range=[0.01, 2.0],
        #     color=BLUE
        # )

        # Taylorpolynom_1 Grad = 1 + x
        def t_1(x):
            return 1 + x
        graph_t1 = axes.plot(t_1, color=RED, x_range=[-2.0, 2.0])
        label_t1 = axes.get_graph_label(graph_t1, label='1. Grad Taylor',direction=UP).scale(0.7)

        # Restglied
        def r_1(x):
            return (np.exp(x) / 2) * (x**2)
        graph_r1 = axes.plot(r_1, color=GREEN, x_range=[-2.0, 1.5])
        label_r1 = axes.get_graph_label(graph_r1, label='1. Grad Restglied', direction=UP).scale(0.7)

        #Tolerenz = 0.1, Highlight regions where |R1(x)| < 0.1
        def highlight_region(x):
            return abs(r_1(x)) < 0.1
        # Highlight regions
        highlighted_regions = VGroup()
        for x in np.linspace(-2.0, 2.0, 100):
            if highlight_region(x):
                dot = Dot(axes.c2p(x, r_1(x)), color=ORANGE, radius=0.05)
                highlighted_regions.add(dot)

        # Animate
        self.add(grid, axes)
        self.play(Create(point))
        self.play(Create((graph_exp), run_time =2.0))
        self.play(Write(label_exp), run_time=1.0)
        self.wait(1)
        self.play(Create(graph_t1), run_time = 2.0)
        self.play(Write(label_t1), run_time=1.0)
        self.wait(2)
        self.play(Create(graph_r1), run_time = 2.0)
        self.play(Write(label_r1), run_time=1.0)
        self.wait(2)
        self.play(FadeIn(highlighted_regions), run_time=2.0)
        self.wait(2)
