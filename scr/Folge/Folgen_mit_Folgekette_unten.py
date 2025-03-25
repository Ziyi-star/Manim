from manim import *

config.background_color = WHITE

class FolgenMitFolgekette(Scene):
    def construct(self):
        # Define the elements with subscripts
        elements = [
            ("a", 1),  # (element, subscript)
            ("a", 2),
            ("a", 3),
            ("a", 4),
            ("a", 5),
            ("a", 6),
            ("a", 7),
            ("...", "")
        ]
        
        # Horizontal chain
        circles = []
        labels = []
        for elem, sub in elements:
            # Create a circle with white fill and black outline
            circle = Circle(radius=0.5, color=BLACK, fill_color=WHITE, fill_opacity=0.5)

            # Create the label inside the circle (e.g., a₁)
            label = MathTex(f"{elem}_{{{sub}}}", font_size=20, color=BLACK)
            label.move_to(circle.get_center())
            # Add to lists
            circles.append(circle)
            labels.append(label)
        
        # Arrange the circles in a horizontal chain
        lines = []
        for i in range(1, len(circles)):
            circles[i].next_to(circles[i-1], RIGHT, buff=0.5)
            labels[i].move_to(circles[i].get_center())
            if i > 0:
                # Draw a line between the current and previous circle
                line = Line(
                    circles[i-1].get_right(),
                    circles[i].get_left(),
                    color=BLACK
                )
                lines.append(line)
        
        # Center the entire chain on the screen
        group = VGroup(*circles, *labels, *lines)
        group.to_corner(DL, buff=1)
        
        # appear circles labels lines all at once
        self.play(Create(group), run_time=2)
        self.wait(1)
        
        # Vertical chain 0
        elements_b = [
            ("...", ""),  # (element, subscript)
            ("...", ""),
            ("...", ""),
            ("...", "")
        ]
        # Create new circles and labels for each new element
        circles_b = []
        labels_b = []
        for elem, sub in elements_b:
            # Create a circle with white fill and black outline
            circle = Circle(radius=0.3, color=BLACK, fill_color=ORANGE, fill_opacity=0.5)

            # Create the label inside the circle (e.g., b₁)
            label = MathTex(f"{elem}_{{{sub}}}", font_size=20, color=BLACK)
            label.move_to(circle.get_center())
            # Add to lists
            circles_b.append(circle)
            labels_b.append(label)
        # Arrange the new circles in a vertical chain starting from the first circle
        lines_b = []
        for i in range(len(circles_b)):
            if i == 0:
                circles_b[i].next_to(circles[0], UP, buff=0.5)
            else:
                circles_b[i].next_to(circles_b[i-1], UP, buff=0.5)
            labels_b[i].move_to(circles_b[i].get_center())
            if i > 0:
                # Draw a line between the current and previous new circle
                line = Line(
                    circles_b[i-1].get_top(),
                    circles_b[i].get_bottom(),
                    color=BLACK
                )
                lines_b.append(line)
        # Draw a line from the first circle in the horizontal chain to the first circle in the vertical chain
        connecting_line_b = Line(
            circles[0].get_top(),
            circles_b[0].get_bottom(),
            color=BLACK
        )
        self.play(Create(connecting_line_b), run_time=0.5)
        # Animate the new circles, labels, and lines appearing one by one
        for i in range(len(circles_b)):
            self.play(
                Create(circles_b[i]),
                Write(labels_b[i]),
                run_time=0.5
            )
            if i > 0:
                self.play(Create(lines_b[i-1]), run_time=0.5)
        self.wait(1)


        # Vertical chain 1
        elements_c = [
            ("...", ""),  # (element, subscript)
            ("...", ""),
            ("...", ""),
            ("...", "")
        ]
        # Create new circles and labels for each new element
        circles_c = []
        labels_c = []
        for elem, sub in elements_c:
            # Create a circle with white fill and black outline
            circle = Circle(radius=0.3, color=BLACK, fill_color=GREEN, fill_opacity=0.5)
            # Create the label inside the circle (e.g., b₁)
            label = MathTex(f"{elem}_{{{sub}}}", font_size=20, color=BLACK)
            label.move_to(circle.get_center())
            # Add to lists
            circles_c.append(circle)
            labels_c.append(label)
        # Arrange the new circles in a vertical chain starting from the first circle
        lines_c = []
        for i in range(len(circles_c)):
            if i == 0:
                circles_c[i].next_to(circles[1], UP, buff=0.5)
            else:
                circles_c[i].next_to(circles_c[i-1], UP, buff=0.5)
            labels_c[i].move_to(circles_c[i].get_center())
            if i > 0:
                # Draw a line between the current and previous new circle
                line = Line(
                    circles_c[i-1].get_top(),
                    circles_c[i].get_bottom(),
                    color=BLACK
                )
                lines_c.append(line)
        # Draw a line from the first circle in the horizontal chain to the first circle in the vertical chain
        connecting_line_c = Line(
            circles[1].get_top(),
            circles_c[0].get_bottom(),
            color=BLACK
        )
        self.play(Create(connecting_line_c), run_time=0.3)
        # Animate the new circles, labels, and lines appearing one by one
        for i in range(len(circles_c)):
            self.play(
                Create(circles_c[i]),
                Write(labels_c[i]),
                run_time=0.5
            )
            if i > 0:
                self.play(Create(lines_c[i-1]), run_time=0.2)
        self.wait(1)

        