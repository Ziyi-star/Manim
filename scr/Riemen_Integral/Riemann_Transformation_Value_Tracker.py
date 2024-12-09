from manim import *

class RiemannTransformation(Scene):
    def construct(self):
        # Coordinate system
        ax = Axes(
            x_range=[-1, 5, 1],
            y_range=[-1, 20, 2],
            x_length=10,
            y_length=10,
            axis_config={"tip_shape": StealthTip},
        ).to_edge(DOWN).add_coordinates()

        # Labels for axes
        labels = ax.get_axis_labels(
            Tex("x"), Tex("y")
        )


        # Function
        func = ax.plot(lambda x: x**2, color=BLUE)
        func_label = MathTex("f(x) = x^2").to_corner(UL)

        # ValueTracker for dynamic dx
        dx_value = ValueTracker(0.2)

        # Riemann Rectangles
        riemann_rects = always_redraw(lambda: ax.get_riemann_rectangles(
            graph=func,
            #start at 0.2 and end at 4 of x range
            x_range=[0.2, 4],
            dx=dx_value.get_value(),
            stroke_width=0.5,
            stroke_color=WHITE,
            fill_opacity=0.75,
            color=(YELLOW, ORANGE)
        ))

        # Fill the area under the curve between x=0 and x=4
        filled_area = ax.get_area(
            graph=func,
            x_range=[0, 4],
            color=ORANGE,
            opacity=0.6
        )

        # Add elements to the scene
        self.add(ax, func, func_label, labels, riemann_rects)

        # Animate the shrinking of dx (value tracker start from 0.2, end at 0.05)
        self.play(dx_value.animate.set_value(0.05), run_time=10, rate_func=smooth)
        self.wait()


        # Transition from Riemann rectangles to full fill
        self.play(
            FadeOut(riemann_rects, run_time=3),  # Fade out the rectangles
            filled_area.animate.set_opacity(0.6),  # Fade in the filled area
        )
        self.wait()
