from manim import *
import math

class FolgenSchlange(Scene):
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
        
        # Arrange the circles along a snake-like (curved) path.
        # They will also become smaller the further along the chain.
        for i, circle in enumerate(circles):
            # Compute a shrinking scale factor (stop at a minimum scale)
            scale_factor = max(1 - 0.04 * i, 0.5)
            circle.scale(scale_factor)
            labels[i].scale(scale_factor)
            # Compute positions: x increases linearly; y oscillates in a sine wave.
            x_offset = i * (circle.width + 0.3)
            y_offset = 0.5 * math.sin(i * 0.8)  # adjust frequency/amplitude as desired
            # Set each circle's center position. Adjust the starting position if needed.
            circle.move_to(np.array([x_offset, y_offset, 0]))
            labels[i].move_to(circle.get_center())
            
        
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