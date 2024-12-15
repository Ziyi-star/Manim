from manim import *

class Mittelwertsatz(Scene):
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

        # Axes
        ax = Axes(
            x_range=[-1, 10, 1],
            y_range=[-1, 5, 1],
            x_length=11,
            y_length=7,
            axis_config={"color": WHITE},
            tips=True,
        ).to_edge(UP).add_coordinates()

        # Labels
        x_label = ax.get_x_axis_label(Tex("x").scale(0.7))
        y_label = ax.get_y_axis_label(Tex("f(x)").scale(0.7))

        # Define the curve
        f = lambda x: 0.1 * (x - 3)**3 + 1
        curve = ax.plot(f, color=BLUE)

        # Interval [a, b]
        a = 2
        b = 6

        # Filled area under the curve
        filled_area = ax.get_area(
            graph=curve,
            x_range=[a, b],
            color=GREEN,
            opacity=0.6
        )

        # ValueTracker for moving xi
        xi_tracker = ValueTracker(4.4)

        # Dynamic dot at xi
        xi_dot = always_redraw(lambda: Dot(
            ax.c2p(xi_tracker.get_value(), f(xi_tracker.get_value())),
            color=RED
        ))

        # Dynamic rectangle with the bottom edge aligned to the x-axis
        rectangle = always_redraw(lambda: Rectangle(
            width=ax.c2p(b, 0)[0] - ax.c2p(a, 0)[0],  # Width: b - a
            height=f(xi_tracker.get_value())+0.2,         # Height at f(ξ)
            color=BLUE,
            fill_opacity=0.5,
        ).move_to(ax.c2p((a + b) / 2, 0), DOWN))  # Align bottom edge at y=0 (x-axis)


        # Dynamic vertical line at xi
        xi_line = always_redraw(lambda: ax.get_vertical_line(
            ax.c2p(xi_tracker.get_value(), f(xi_tracker.get_value())),
            color=BLACK
        ))

        # Add elements to the scene
        self.play(Create(grid))
        self.play(Create(ax))
        self.play(Write(x_label), Write(y_label))
        self.play(Create(curve))
        self.play(Create(filled_area))
        self.play(Create(rectangle), Create(xi_line), Create(xi_dot))

        # 1. Move xi_dot and rectangle from xi = 4.4 to 5
        self.play(xi_tracker.animate.set_value(5), run_time=3, rate_func=linear)
        self.wait(1)

        # 2. Move xi_dot and rectangle back from xi = 4.9 to 4.5
        self.play(xi_tracker.animate.set_value(4.5), run_time=3, rate_func=linear)
        self.wait(1)

        # 3. Move to the final point at xi = 4.8
        self.play(xi_tracker.animate.set_value(4.8), run_time=2, rate_func=smooth)
        self.wait(2)
