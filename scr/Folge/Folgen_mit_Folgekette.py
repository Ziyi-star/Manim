from manim import *

config.background_color = WHITE

class FolgenMitFolgekette(Scene):
    def construct(self):
        # Horizontal chain
        main_circles = []
        labels_in = []
        labels_out = []
        for i in range(8):
            # Create a circle with white fill and black outline
            circle = Circle(radius=0.5, color=BLACK, fill_color=WHITE, fill_opacity=1)
            # Create the label inside the circle (e.g., a₁)
            if i < 7:
                label = MathTex("a_{\\mathbf{" + str(i+1) + "}}", font_size=25, color=BLACK)
                label_out = MathTex(f"n = {i+1}", font_size=30, color=BLACK)
                main_circles.append(circle)
                labels_in.append(label)
                labels_out.append(label_out)
            if i == 7:
                label = MathTex(f"...", font_size=20, color=BLACK)
                label_out = MathTex(f"...", font_size=30, color=BLACK)
                main_circles.append(circle)
                labels_in.append(label)
                labels_out.append(label_out)
        
        # Arrange the circles in a parabolic shape
        a = -0.03  # Reduced coefficient for flatter curve
        x_spacing = 1.5  # Increased spacing for better visibility
        x_shift = (len(main_circles) - 1) * x_spacing / 2  # Center horizontally
        y_shift = 2  # Increased vertical offset

        lines = []
        for i in range(len(main_circles)):
            # Calculate position on parabola
            x = i * x_spacing - x_shift
            y = a * x**2 + y_shift
            
            # Move circle and label to calculated position
            main_circles[i].move_to([x, y, 0])
            labels_in[i].move_to(main_circles[i].get_center())
            labels_out[i].move_to(main_circles[i].get_top() + 0.3 * UP)
            
            # Create lines between circles
            if i > 0:
                line = Line(
                    main_circles[i-1].get_center(),
                    main_circles[i].get_center(),
                    color=BLACK
                )
                lines.append(line)

        # Group everything together
        group = VGroup(*lines, *main_circles, *labels_in, *labels_out)
        group.to_edge(UP)  # Move to bottom with some padding
        
        # appear circles labels lines all at once
        self.play(Create(group), run_time=2)
        self.wait(1)

        def create_vertical_chain(main_circle, circle_color=ORANGE,bold_num=1):
            """
            Creates a vertical chain of circles connected to a main circle.
            
            Args:
                main_circle: The circle to connect the vertical chain to
                circle_color: Color of the circles
                
            Returns:
                A tuple containing (circles, labels, lines, connecting_line) for the new little chain
            """
            ellipses = []
            labels = []
            
            # Create circles and labels
            for i in range(5):
                ellipse = Ellipse(
                    width=0.6,
                    height=0.7,
                    color=BLACK,
                    fill_color=circle_color,
                    fill_opacity=0.5
                )
                if i != 4:
                    label = MathTex(f"a_{{\\mathbf{{{bold_num}}}{i+1}}}", font_size=25, color=BLACK)
                if i == 4:
                    label = MathTex(f"...", font_size=20, color=BLACK)
                ellipses.append(ellipse)
                labels.append(label)
            
            # Position circles and create connecting lines
            lines = []
            for i in range(len(ellipses)):
                if i == 0:
                    ellipses[i].next_to(main_circle, DOWN, buff=0.3)
                else:
                    ellipses[i].next_to(ellipses[i-1], DOWN, buff=0.2)
                labels[i].move_to(ellipses[i].get_center())
                
                if i > 0:
                    line = Line(
                        ellipses[i-1].get_bottom(),
                        ellipses[i].get_top(),
                        color=BLACK
                    )
                    lines.append(line)
            
            # Create connecting line to main circle
            connecting_line = Line(
                main_circle.get_bottom(),
                ellipses[0].get_top(),
                color=BLACK
            )
            
            return ellipses, labels, lines, connecting_line
                
        # Vertical chain 1
        circles_one, labels_one, lines_one, connecting_line_one = create_vertical_chain(
            main_circle=main_circles[0],
            circle_color=ORANGE, 
            bold_num=1
        )
        # Animation
        self.play(main_circles[0].animate.set_fill(ORANGE, 1), run_time=0.5)
        self.play(Create(connecting_line_one), run_time=0.5)
        for i in range(len(circles_one)):
            self.play(
                Create(circles_one[i]),
                Write(labels_one[i]),
                run_time=0.5
            )
            if i > 0:
                self.play(Create(lines_one[i-1]), run_time=0.5)
        self.wait(1)

        # Vertical chain 2
        circles_two, labels_two, lines_two, connecting_line_two = create_vertical_chain(
            main_circle=main_circles[1],
            circle_color=GREEN,
            bold_num=2
        )
        # Animation
        self.play(main_circles[1].animate.set_fill(GREEN, 1), run_time=0.5)
        self.play(Create(connecting_line_two), run_time=0.5)
        for i in range(len(circles_two)):
            self.play(
                Create(circles_two[i]),
                Write(labels_two[i]),
                run_time=0.5
            )
            if i > 0:
                self.play(Create(lines_two[i-1]), run_time=0.3)
        self.wait(1)

        # Vertical chain 3
        circles_three, labels_three, lines_three, connecting_line_three = create_vertical_chain(
            main_circle=main_circles[2],
            circle_color=BLUE,
            bold_num=3
        )
        # Animation
        self.play(main_circles[2].animate.set_fill(BLUE, 1), run_time=0.5)
        self.play(Create(connecting_line_three), run_time=0.5)
        for i in range(len(circles_three)):
            self.play(
                Create(circles_three[i]),
                Write(labels_three[i]),
                run_time=0.5
            )
            if i > 0:
                self.play(Create(lines_three[i-1]), run_time=0.2)
        self.wait(1)

        