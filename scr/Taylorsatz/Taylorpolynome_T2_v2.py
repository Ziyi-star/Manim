from manim import *
from matplotlib.pyplot import axes

class TaylorpolynomeT2V2(ZoomedScene):
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
        # Create a label "0" at the origin
        zero_label = MathTex("0").next_to(axes.c2p(0, 0), DOWN, buff=0.1)

                
        legend = Rectangle(
            color=WHITE,
            width=4.0,
            height=4.5,
        ).to_corner(UP + LEFT, buff=0.5)

        def exp_func(x):
            return np.exp(x)
        
        graph_exp = axes.plot(exp_func, color=BLUE, x_range=[-2.0, 2.0])
        label_exp = MathTex("f(x) = e^x", color=BLUE).move_to(legend.get_center() + UP * 1.7).scale(0.9)

        # Taylorpolynom_2 Grad = 1 + x + x^2/2
        def t_2(x):
            return 1 + x + (x**2) / 2
        graph_t2 = axes.plot(t_2, color=RED, x_range=[-2.0, 2.0])
        label_t2 = MathTex("T_2(x) = 1 + x + \\frac{x^2}{2}", color=RED).next_to(label_exp, DOWN).scale(0.9)
        
        # Restglied
        def r_2(x):
            return exp_func(x) - (t_2(x))
        graph_r2 = axes.plot(r_2, color=GREEN, x_range=[-2.0, 2.0])
        label_r2 = MathTex("R_2(x) = f(x) - T_2(x)", color=GREEN).next_to(label_t2, DOWN).scale(0.9)

        #Tolerenz = 0.1, Highlight regions where |R2(x)| < 0.1
        def highlight_region(x):
            return abs(r_2(x)) < 0.1
        # Highlight regions
        highlighted_regions_rest_2 = VGroup()
        highlighted_regions_taylor_2 = VGroup()
        xs_within = []
        for x in np.linspace(-2.0, 2.0, 100):
            if highlight_region(x):
                xs_within.append(x)
                dot_r2 = Dot(axes.c2p(x, r_2(x)), color=ORANGE, radius=0.05)
                dot_t2 = Dot(axes.c2p(x, t_2(x)), color=YELLOW, radius=0.05)
                highlighted_regions_rest_2.add(dot_r2)
                highlighted_regions_taylor_2.add(dot_t2)
        if xs_within:
            left_x = min(xs_within)
            right_x = max(xs_within)
            mid_x = (left_x + right_x) / 2

        label_x0 = MathTex("x_0 = 0", color=WHITE).next_to(label_r2, DOWN).scale(0.9)
        # highlighted_regions Tolerenz < 0.1, Highlight regions where |R2(x)| < 0.1
        #todo: allways redraw 1. label x, r2(x), gleichzeitig auf x Achse betont 
        x_tracker = ValueTracker(left_x)
        dot_on_x = always_redraw(
            lambda: Dot(axes.c2p(x_tracker.get_value(), 0), color=YELLOW)
        )
        label_x = always_redraw(
            lambda: MathTex(f"x = {x_tracker.get_value():.2f}")
                        .next_to(label_x0, DOWN)
        ).scale(0.9).set_color(YELLOW)
        label_

        # Animate
        self.add(grid, axes,zero_label)
        self.play(Create((graph_exp), run_time =2.0))
        self.play(Create(legend), run_time=1.0)
        self.play(FadeIn(label_exp), run_time=1.0)
        #self.wait(1)
        self.play(Create(graph_t2), run_time = 2.0)
        self.play(FadeIn(label_t2), run_time=1.0)
        #self.wait(2)
        self.play(Create(graph_r2), run_time=2.0)
        self.play(FadeIn(label_r2), run_time=1.0)
        #self.wait(2)
        self.play(FadeIn(label_x0), run_time=1.0)
        self.play(FadeIn(label_x), run_time=1.0)       
        # Highlight: Animate x_tracker to the right_x value
        self.add(dot_on_x)
        self.play(x_tracker.animate.set_value(right_x), run_time=4.0)
        self.wait(2)

        # self.play(FadeIn(highlighted_regions_rest_2), run_time=2.0)
        # self.wait(2)
        # self.play(FadeIn(highlighted_regions_taylor_2, run_time=2.0))
        # # zoom in on the highlighted regions
        # self.play(self.camera.frame.animate.scale(1/2).move_to(axes.c2p(mid_x, 0)))  # Zoom in
        # self.wait(5)
        #  # Reset the camera to its original position
        # self.play(self.camera.frame.animate.scale(2).move_to(ORIGIN))  # Zoom out
        # self.wait(2)
       
