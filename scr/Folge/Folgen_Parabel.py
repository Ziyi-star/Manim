from manim import *

config.background_color = WHITE

class FolgenParabel(Scene):
    def construct(self):

        # Add a title
        title = Text("Folgen", font_size=60, color=BLACK)
        title.to_edge(UP)
        self.add(title)

        # Define the elements with subscripts
        elements = [
            ("a", 1),  # (element, subscript)
            ("a", 2),
            ("a", 3),
            ("a", 4),
            ("a", 5),
            ("a", 6),
            ("a", 7),
            ("...",""),
        ]
        
        num_circles = 8
        circles = []
        labels = []

        for i in range(num_circles):
            radius = 1
            circle = Circle(radius=radius, color=BLACK, fill_color=WHITE, fill_opacity=1)
            label = MathTex(f"a_{{{i+1}}}", font_size=20, color=BLACK)
            label.move_to(circle.get_center())

            circles.append(circle)
            labels.append(label)

        # Arrange circles in a parabolic shape
        a = 0.1
        for i in range(num_circles):
            x = i * 0.6
            y = a * (x - 6) ** 2  # Adjust shift (6) to center the parabola
            circles[i].move_to([x, y, 0])
            labels[i].move_to(circles[i].get_center())

        group = VGroup(*circles, *labels)
        group.to_corner(UL).next_to(title, DOWN, buff=0.5)

        # Animate lines between circles
        lines = VGroup()
        for i in range(1, num_circles):
            lines.add(Line(circles[i-1].get_center(), circles[i].get_center(), color=BLACK))
        self.play(Create(lines), run_time=0.5)

        # Animate circles and labels
        for i in range(num_circles):
            self.play(Create(circles[i]), Write(labels[i]), run_time=0.3)

        self.wait(2)