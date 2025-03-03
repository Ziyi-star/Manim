from manim import *

class Folgen(Scene):
    def construct(self):
        # Load the background image
        background = ImageMobject("Hintergrundbild.jpg")
        background.scale_to_fit_height(config.frame_height)
        background.scale_to_fit_width(config.frame_width)
        self.add(background)

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
            ("a", 8),
            ("a", 9),  # (element, subscript)
            ("a", 10),
            ("a",11),
            ("a", 12),
            ("a", 13),
            ("a", 14),
            ("a", 15),
            ("a", 16),
        ]
        
        # Create circles and labels for each element
        circles = []
        labels = []
        for elem, sub in elements:
            # Create a circle with white fill and black outline
            circle = Circle(radius=0.2, color=BLACK, fill_color=WHITE, fill_opacity=0.5)

            # Create the label inside the circle (e.g., a₁)
            label = MathTex(f"{elem}_{{{sub}}}", font_size=20, color=BLACK)
            label.move_to(circle.get_center())
            # Add to lists
            circles.append(circle)
            labels.append(label)
        
        # Arrange the circles in a horizontal chain
        for i in range(1, len(circles)):
            circles[i].next_to(circles[i-1], RIGHT, buff=0.3)
            labels[i].move_to(circles[i].get_center())
        
        # Center the entire chain on the screen
        group = VGroup(*circles, *labels)
        group.to_corner(UL).next_to(title, DOWN, buff=0.5)
        
        # Animate the circles and labels appearing one by one
        for i in range(len(circles)):
            self.play(
                Create(circles[i]),
                Write(labels[i]),
                run_time=0.5
            )
            if i > 0:
                # Draw a line between the current and previous circle
                line = Line(
                    circles[i-1].get_right(),
                    circles[i].get_left(),
                    color=BLACK
                )
                self.play(Create(line), run_time=0.5)

        # Wait for a moment at the end
        self.wait(2)