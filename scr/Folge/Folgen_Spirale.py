from manim import *
import numpy as np

config.background_color = WHITE

class FolgenSpirale(Scene):
    def construct(self):
        circles = VGroup()
        front_labels = VGroup() 
        back_labels = VGroup()
        num_circles = 50  # Mehr Kreise

        angle_offset = -0.8  # Radians (z.B. ~-45°)

        for i in range(num_circles):
            # Kleinerer Multiplikator für eine engere Spiralbahn
            t = (num_circles - i - 1) * 0.2
            
            # Radius etwas kleiner halten, damit die Kreise weniger wachsen
            radius = 0.04 + (num_circles - i - 1) * 0.007
            
            x = (0.5 + 0.35 * t) * np.cos(t+angle_offset)
            # +1 als Offset, um die Spirale etwas anzuheben
            y = -(0.5 + 0.35 * t) * np.sin(t+angle_offset) + 1
            
            circle = Circle(radius=radius, color=BLACK, fill_color=WHITE, fill_opacity=0.5)
            circle.move_to([x, y, 0])

            # Create label
            if i < 10:
                front_label_text = f"a_{{{i+1}}}"  # Creates a₁, a₂, etc.
                back_label_text = f"{i+1}"
            if i >= 10 and i <= 12:
                front_label_text = "..."
                back_label_text = "..."
            if i == 13:
                front_label_text = "a_{n-1}"
                back_label_text = "n-1"
            if i == 14:
                front_label_text = "a_n"
                back_label_text = "n"
            if i > 14:
               front_label_text = "..."  
               back_label_text = "..."

            # Create label
            front_label = MathTex(front_label_text, color=BLACK, font_size=20)
            front_label.move_to(circle.get_center())
            back_label = MathTex(back_label_text, color=BLACK, font_size=20)
            back_label.move_to(circle.get_center())

            circles.add(circle)
            front_labels.add(front_label)
            back_labels.add(back_label)
        
        self.play(Create(circles), run_time=4)
        self.play(Write(front_labels), run_time=8)
        self.wait(2)

        # Flip each circle and switch labels
        for i in range(len(circles)):
            circle = circles[i]
            front_label = front_labels[i]
            back_label = back_labels[i]
            
            # Hide back label initially
            back_label.set_opacity(0)
            self.add(back_label)

            # Flip animation
            self.play(
                Rotate(
                    circle,
                    angle=PI,
                    axis=RIGHT,
                    about_point=circle.get_center()
                ),
                front_label.animate.set_opacity(0),  # Fade out front label
                back_label.animate.set_opacity(1),   # Fade in back label
                run_time=0.5
            )
        
        self.wait(2)

       

