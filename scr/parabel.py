from manim import *

class Parabel(Scene):
    def construct(self):
        #Kooridinatensystem
        plane = NumberPlane(x_range=[-5, 5, 1], x_length=7,
                            y_range=[-5, 5, 1],y_length=7).add_coordinates()
        
        labels = plane.get_axis_labels(x_label = "x", y_label="f(x)")

        parabel_exp = plane.plot(lambda x: x**2-x-3, x_range=[-5, 5], color=BLUE)
        parabel_exp_label = MathTex("f(x) = x^2-x-3").to_corner(UL)

        self.play(DrawBorderThenFill(plane))
        self.play(Create(VGroup(parabel_exp,labels,parabel_exp_label)))
        self.wait()