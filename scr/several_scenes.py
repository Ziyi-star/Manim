from manim import *
from hello import *
from draw_name_circle_triangle import *
from ableitung import *


class Several_scenes(Scene):
    def construct(self):
        Hello(self)
        Name_Rectangle(self)
        Ableitung(self)