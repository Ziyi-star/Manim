from manim import *

class Integral_Parabel(Scene):
    def construct(self):
        #Kooridinatensystem
        plane = NumberPlane(x_range=[-5, 5, 1], x_length=7,
                            y_range=[-5, 5, 1],y_length=7).add_coordinates()
        
        labels = plane.get_axis_labels(x_label = "x", y_label="f(x)")

        #parabel
        parabel_exp = plane.plot(lambda x: x**2-x-3, x_range=[-5, 5], color=BLUE)
        parabel_exp_label = MathTex("f(x) = x^2-x-3").to_corner(UL)

        #rieman Rectangle
        area = plane.get_riemann_rectangles(graph=parabel_exp, x_range=[-2, 3], dx=0.2, stroke_width=0.5,stroke_color=BLUE)


        self.play(DrawBorderThenFill(plane))
        self.play(Create(VGroup(labels,parabel_exp_label)))
        self.play(Create(parabel_exp),run_time = 3)
        self.wait()
        self.play(Create(area),run_time = 5)
        self.wait()