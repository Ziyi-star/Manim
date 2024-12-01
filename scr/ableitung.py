from manim import *

class Ableitung(Scene):
    def construct(self):
        ax = Axes(
            x_range=[-4, 4,1],
            y_range=[-2, 16,1],
            x_length=10,
            y_length=6,
            axis_config={'tip_shape': StealthTip},
            ).to_edge(DOWN).add_coordinates()
        
        labels = ax.get_axis_labels(
            Tex("x"), Tex("y")
        )
        func = ax.plot(lambda x: x**2, color=BLUE)

        slope = ax.get_secant_slope_group(
            x=3,
            graph=func,
            dx = 0.6,
            dx_line_color=GREEN,
            dy_line_color=YELLOW,
            secant_line_color = RED,
            secant_line_length=3)


        slope_label = MathTex("\\text{Steigung: }", "4").to_corner(UL)

        self.add(ax, func,slope,slope_label,labels)
        self.wait()

