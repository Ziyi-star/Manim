from manim import *

class Ableitung(Scene):
    def construct(self):

        #Kooridinatensystem
        ax = Axes(
            x_range=[-4, 4,1],
            y_range=[-2, 20,2],
            x_length=10,
            y_length=6,
            axis_config={'tip_shape': StealthTip},
            ).to_edge(DOWN).add_coordinates()
        
        #labels for x,y Achses
        labels = ax.get_axis_labels(
            Tex("x"), Tex("y")
        )

        #function
        func = ax.plot(lambda x: x**2, color=BLUE)

        #change the value of x
        x_change = ValueTracker(-4)

        #ableitung
        slope = always_redraw (lambda:
        ax.get_secant_slope_group(
            x=x_change.get_value(),
            graph=func,
            dx = 0.5,
            dx_line_color=GREEN,
            dy_line_color=YELLOW,
            dx_label=Tex("dx = 0.5").scale(3.0),
            dy_label=Tex("dy").scale(2.9),
            secant_line_color = RED,
            secant_line_length=3)
        )


        #show punkt in graph
        punkt = always_redraw(lambda: Dot(ax.coords_to_point(x_change.get_value(), func.underlying_function(x_change.get_value())), color=RED))

        self.add(ax, func,slope,labels,punkt)
        self.wait()
        self.play(x_change.animate.set_value(4), run_time=10, rate_func=smooth)
        self.wait()


