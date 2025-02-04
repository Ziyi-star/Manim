from manim import *

class Test(ZoomedScene):
    def construct(self):
        Text_1 = Text("Epsilon-Delta-Kriterium in Unstetigkeit", font_size=36, color=YELLOW)

        self.play(Write(Text_1))
        self.wait(2)
        self.remove(Text_1)





