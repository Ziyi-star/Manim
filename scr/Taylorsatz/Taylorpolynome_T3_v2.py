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

        def exp_func(x):
            return np.exp(x)
        
        graph_exp = axes.plot(exp_func, color=WHITE, x_range=[-2.0, 2.0])
        label_exp = MathTex("f(x) = e^x", color=WHITE).to_corner(UP + LEFT*1.5).scale(0.7)

        # Taylorpolynom_3 Grad = 1 + x + x^2/2 + x^3/6
        def t_3(x):
            return 1 + x + (x**2) / 2 + (x**3) / 6
        graph_t3 = axes.plot(t_3, color=BLUE, x_range=[-2.0, 2.0])
        label_t3 = MathTex("T_3(x) = 1 + x + \\frac{x^2}{2} + \\frac{x^3}{6}", color=BLUE).next_to(label_exp, DOWN).scale(0.7)

        # Restglied
        def r_3(x):
            return abs(exp_func(x) - (t_3(x)))
        graph_r3 = axes.plot(r_3, color=ORANGE, x_range=[-2.0, 2.0])
        label_r3 = MathTex(r"R_3(x) = |f(x) - T_3(x)|", color=ORANGE).next_to(label_t3, DOWN).scale(0.7)

        #Tolerenz = 0.1, Highlight regions where |R3(x)| < 0.1
        xs_within = [x for x in np.linspace(-2.0, 2.0, 100) if abs(r_3(x)) < 0.1]
        if xs_within:
            left_x, right_x = min(xs_within), max(xs_within)
            mid_x = (left_x + right_x) / 2
        
        # Create labels for left_x and right_x
        label_left_x = MathTex(f"{left_x:.2f}", color=GREEN).scale(0.7)
        label_right_x = MathTex(f"{right_x:.2f}", color=GREEN).scale(0.7)

        # Create arrows pointing to the positions on the x-axis
        arrow_left_x = Arrow(
            start=axes.c2p(left_x, -0.5),  # Start slightly below the x-axis
            end=axes.c2p(left_x, 0),      # End at the x-axis
            color=ORANGE
        )
        arrow_right_x = Arrow(
            start=axes.c2p(right_x, -0.5),  # Start slightly below the x-axis
            end=axes.c2p(right_x, 0),       # End at the x-axis
            color=ORANGE
        )
        # Position labels near the arrows
        label_left_x.next_to(arrow_left_x.get_start(), DOWN, buff=0.2)
        label_right_x.next_to(arrow_right_x.get_start(), DOWN, buff=0.2)

        label_x0 = MathTex("x_0 = 0", color=WHITE).next_to(label_r3, DOWN).scale(0.7)
        x_tracker = ValueTracker(left_x)
        #Labels
        label_x = always_redraw(
            lambda: MathTex(f"x = {x_tracker.get_value():.2f}")
                        .set_color(GREEN)
                        .scale(0.7)
                        .next_to(label_x0, DOWN)
        )
        label_r3_wert = always_redraw(
            lambda: MathTex(
                f"={(r_3(x_tracker.get_value())):.3f}"
            ).set_color(ORANGE)
            .next_to(label_r3, RIGHT,buff=0.01).scale(0.7)
        )
        
        # Line on x achse and area between curves
        def create_highlighted_elements(left_x, color):
            line_on_x_achse = always_redraw(
                lambda: Line(
                    axes.c2p(left_x, 0),
                    axes.c2p(x_tracker.get_value(), 0),
                    color=color,
                )
            )
            area_between_curves = always_redraw(
                lambda: axes.get_area(
                    graph_exp,
                    x_range=[left_x, x_tracker.get_value()],
                    bounded_graph=graph_t3,
                    color=color,
                    opacity=0.7,
                )
            )
            line_vertical = always_redraw(
                lambda: Line(
                    axes.c2p(x_tracker.get_value(), exp_func(x_tracker.get_value())),
                    axes.c2p(x_tracker.get_value(), t_3(x_tracker.get_value())),
                    color=RED,
                    stroke_width=3.0,
                )
            )

             # Create an arrow pointing to the vertical line
            arrow_below_line = always_redraw(
                lambda: Arrow(
                    start=axes.c2p(x_tracker.get_value(), -0.5),  # Start below the x-axis
                    end=axes.c2p(x_tracker.get_value(), 0),      # End at the x-axis
                    color=ORANGE
                )
            )

            # Create a label "|Rn(x)|" below the arrow
            label_rn = always_redraw(
                lambda: MathTex(r"|R_n(x)|", color=ORANGE).next_to(arrow_below_line.get_start(), DOWN, buff=0.2).scale(0.7)
            )
            return line_on_x_achse, area_between_curves, line_vertical, arrow_below_line, label_rn

        # For better visualization for right area
        def create_highlighted_elements_version_2(left_x, color):
            line_on_x_achse = always_redraw(
                lambda: Line(
                    axes.c2p(left_x, 0),
                    axes.c2p(x_tracker.get_value(), 0),
                    color=color,
                )
            )
            area_between_curves = always_redraw(
                lambda: Polygon(
                    *(
                        [axes.c2p(x, exp_func(x)) for x in np.linspace(left_x, x_tracker.get_value(), 200)] +
                        [axes.c2p(x, t_3(x)) for x in np.linspace(x_tracker.get_value(), left_x, 200)]
                    ),
                    color=color,
                    fill_color=color,
                    fill_opacity=0.7,
                    stroke_width=0
                )
            )
            line_vertical = always_redraw(
                lambda: Line(
                    axes.c2p(x_tracker.get_value(), exp_func(x_tracker.get_value())),
                    axes.c2p(x_tracker.get_value(), t_3(x_tracker.get_value())),
                    color=RED,
                    stroke_width=3.0,
                )
            )

            # Create an arrow pointing to the vertical line
            arrow_below_line = always_redraw(
                lambda: Arrow(
                    start=axes.c2p(x_tracker.get_value(), -0.5),  # Start below the x-axis
                    end=axes.c2p(x_tracker.get_value(), 0),      # End at the x-axis
                    color=ORANGE
                )
            )

            # Create a label "|Rn(x)|" below the arrow
            label_rn = always_redraw(
                lambda: MathTex(r"|R_n(x)|", color=ORANGE).next_to(arrow_below_line.get_start(), DOWN, buff=0.2).scale(0.7)
            )
            return line_on_x_achse, area_between_curves, line_vertical, arrow_below_line, label_rn

        # Animate
        self.add(grid, axes,zero_label)
        self.play(Create((graph_exp), run_time =2.0))
        self.play(FadeIn(label_exp), run_time=1.0)
        #self.wait(1)
        self.play(Create(graph_t3), run_time =2.0)
        self.play(FadeIn(label_t3), run_time=1.0)
        #self.wait(2)
        self.play(Create(graph_r3), run_time=2.0)
        self.play(FadeIn(label_r3), run_time=1.0)
        #self.wait(2)
        self.add(label_x0)
        self.add(label_x)
        self.add(label_r3_wert)

        # Scene 1: Animate x_tracker to the right_x value with r_3 < 0.1
        line_on_x_achse, area_between_curves,line_vertical, arrow_below_line, label_rn = create_highlighted_elements(left_x, GREEN)
        self.add(line_on_x_achse, area_between_curves, line_vertical, arrow_below_line, label_rn)
        self.play(x_tracker.animate.set_value(right_x), run_time=10.0, rate=linear)
        self.wait(2)
        # Add labels to the scene
        self.add(arrow_left_x, label_left_x, arrow_right_x, label_right_x)
        self.wait(1)
        #zoom in on the highlighted regions
        self.play(self.camera.frame.animate.scale(1/2).move_to(axes.c2p(mid_x, 0)))  # Zoom in
        self.wait(5)
        # Reset the camera to its original position
        self.play(self.camera.frame.animate.scale(2).move_to(ORIGIN))  # Zoom out
        self.wait(2)
        # remove the highlighted elements
        self.remove(line_on_x_achse, area_between_curves, line_vertical)
        self.wait(1)
        #Scene 2: Animate x_tracker with r_2 > 0.1 left area
        x_tracker = ValueTracker(left_x)
        line_on_x_achse, area_between_curves, line_vertical, arrow_below_line, label_rn = create_highlighted_elements_version_2(left_x, RED_B)
        self.add(line_on_x_achse, area_between_curves, line_vertical, arrow_below_line, label_rn)
        self.play(x_tracker.animate.set_value(-2.0), run_time=8.0, rate=linear)
        self.wait(2)
        self.remove(line_on_x_achse, area_between_curves, line_vertical, arrow_below_line, label_rn)
        self.wait(1)
        # Scene 3: Animate x_tracker with r_2 > 0.1 right area
        x_tracker = ValueTracker(right_x)
        line_on_x_achse, area_between_curves, line_vertical, arrow_below_line, label_rn = create_highlighted_elements_version_2(right_x, RED_B)
        self.add(line_on_x_achse, area_between_curves, line_vertical, arrow_below_line, label_rn)
        self.play(x_tracker.animate.set_value(2.0), run_time=10.0, rate=linear)
        self.wait(2)



       
