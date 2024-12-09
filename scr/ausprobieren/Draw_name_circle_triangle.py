from manim import *


class Name_Rectangle(Scene):
    def construct(self):
        name = Tex("Ziyi Liu").to_edge(UL,buff=0.5)
        #shift from middle to left with size 3
        sq = Square(side_length = 0.5,fill_color = GREEN, fill_opacity = 0.75).shift(LEFT * 3)
        tri = Triangle().scale(0.6).to_edge(DR)


        #just write name, square and triangle
        self.play(Write(name))
        self.play(DrawBorderThenFill(sq),run_time = 2)
        self.play(Create(tri))
        self.wait()

        #do some animations 
        self.play(
            # name move from upperleft to upperright, bigger size of 2
            name.animate.to_edge(UR).scale(2),
            # square bigger from 0.6 to 3 Size
            sq.animate.scale(2),
            # triangle move from downright to downleft
            tri.animate.to_edge(DL).scale(2),
            run_time = 3
        )
        self.wait()

        