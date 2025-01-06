from manim import *

class RiemannTransformation(Scene):
    def construct(self):
         #Text
        text = Text("Integral von f(x) = x²",font_size=36, color=YELLOW)
        # Coordinate system
        ax = Axes(
            x_range=[-3, 5, 1],  # Further extend x_range to fully include y-axis
            y_range=[-1, 15, 2],
            x_length=12,         # Increase length for better visibility
            y_length=8,          # Adjust y_length to maintain proportions
            axis_config={"tip_shape": StealthTip},
        ).move_to(ORIGIN).add_coordinates()  # Center axes in the middle of the screen


        # Labels for axes
        labels = ax.get_axis_labels(
            Tex("x"), Tex("y")
        )

        # Function
        func = ax.plot(lambda x: x**2, color=BLUE, x_range=[0, 5])

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
            color=(YELLOW, GOLD)
        ))

        # Fill the area under the curve between x=0 and x=4
        filled_area = ax.get_area(
            graph=func,
            x_range=[0, 4],
            color=ORANGE,
            opacity=0.6
        )

        # Add elements to the scene
        self.play(Write(text))
        self.wait(2)
        self.play(FadeOut(text))
        self.play(Create(ax))
        self.play(Write(labels))
        self.play(Create(func))
        self.wait(2)
        self.play(Create(riemann_rects))
        self.wait(1)

         # Animate the shrinking of dx
        self.play(dx_value.animate.set_value(0.1), run_time=10, rate_func=smooth)
        self.wait(2)

        self.play(dx_value.animate.set_value(0.05), run_time=10, rate_func=smooth)
        self.wait(2)

        # Pause at final dx and highlight rectangles
        self.play(Indicate(riemann_rects, color=GREEN), run_time=2)
        self.wait(2)

        # Transition from Riemann rectangles to full fill
        self.play(
            FadeOut(riemann_rects, run_time=5),  # Fade out the rectangles
            FadeIn(filled_area, run_time=5),    # Fade in the filled area
        )
        self.wait(3)

        