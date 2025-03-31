import random
from manim import *

config.background_color = WHITE

'''
Name convention:
Circle from first iteration is called first plate, second plate, third plate, etc.
Circle from second iteration is called second one plate, second two plate, etc.
Arrows from first to second iteration are called arrow_first_to_second_one, arrow_first_to_second_two, etc.
Arrows from second to third iteration are called arrow_second_one_to_third_one, arrow_second_one_to_third_two, etc.
'''


class FolgenRekursionHorizontal(Scene):
    def construct(self):
        # Store the first blob's points
        stored_blob_points = None
        
        def create_plate_with_blob(position=ORIGIN):
            nonlocal stored_blob_points  # Add this line to access outer variable
            
            # Create outer circle
            outer_circle = Circle(
                radius=0.3,
                color=BLACK,
                fill_color=WHITE,
                fill_opacity=1,
                stroke_width=4,  # Thicker border for plate edge
            ).move_to(position)

            # Create inner circle
            inner_circle = Circle(
                radius=0.2,
                color=BLACK,
                fill_color=BLUE_B,
                fill_opacity=1,
                stroke_width=2,  # Thinner border for inner rim
            ).move_to(outer_circle.get_center())
            
            # Create irregular shape
            blob = VMobject(color=BLACK, fill_opacity=1)
            if stored_blob_points is not None:
                blob.set_points(stored_blob_points)
            if stored_blob_points is None:
                # Create new blob shape
                radius = 0.05
                num_points = 8
                points = []
                for i in range(num_points):
                    angle = i * TAU / num_points
                    offset = random.uniform(0.7, 1.3)
                    x = radius * np.cos(angle) * offset
                    y = radius * np.sin(angle) * offset
                    points.append([x, y, 0])
                points.append(points[0])  # Close the shape
                blob.set_points_smoothly(points)
                stored_blob_points = blob.get_points()
                
            blob.move_to(inner_circle.get_center())
            plate = VGroup(outer_circle, inner_circle, blob)
            return plate

        # Create the text "Beispiel:"
        beispiel_text = Tex("Beispiel:", color=BLACK, font_size=36).to_edge(UP + LEFT)

        # Create the formula a_{n+1} = 2 \cdot a_n
        formula = MathTex(
            "a_{n+1}", "=", "2", "\\cdot", "a_n",
            font_size=48,
            color=BLACK
        ).next_to(beispiel_text, RIGHT, buff=0.5)

        
        # First iteration Circles
        first_plate = create_plate_with_blob(position=UP*2 + RIGHT*2)
        # label for first plate
        label_first_plate = MathTex("a_1 = p", color=BLACK
            ).next_to(first_plate, LEFT, buff=5.4)

        # Second iteration Circles
        second_one_plate = create_plate_with_blob(
            position=first_plate.get_center() + DOWN * 1 + LEFT * 2
        )
        second_two_plate = create_plate_with_blob(
            position=first_plate.get_center() + DOWN * 1 + RIGHT * 2
        )
        label_second_iteration = MathTex("a_2 = 2a_1", color=BLACK
            ).next_to(second_one_plate, LEFT, buff=3)
        #arrows from first to second iteration
        arrow_first_to_second_one = Arrow(
            start=first_plate.get_left(),
            end=second_one_plate.get_top(),
            color=BLACK,
        )
        arrow_first_to_second_two = Arrow(
            start=first_plate.get_right(), 
            end=second_two_plate.get_top(),
            color=BLACK,
        )
        
        # Third iteration Circles
        third_one_plate = create_plate_with_blob(
            position=second_one_plate.get_center() + DOWN * 1 + LEFT * 1
        )
        third_two_plate = create_plate_with_blob(
            position=second_one_plate.get_center() + DOWN * 1 + RIGHT * 1
        )
        third_three_plate = create_plate_with_blob(
            position=second_two_plate.get_center() + DOWN * 1 + LEFT * 1
        )
        third_four_plate = create_plate_with_blob(
            position=second_two_plate.get_center() + DOWN * 1 + RIGHT * 1
        )
        label_third_iteration = MathTex("a_3 = 2a_2", color=BLACK).next_to(third_one_plate, LEFT, buff=2)
        #arrows from second to third iteration
        arrow_second_one_to_third_one = Arrow(
            start = second_one_plate.get_left(),
            end = third_one_plate.get_top(),
            color = BLACK,
        )
        arrow_second_one_to_third_two = Arrow(
            start = second_one_plate.get_right(),
            end = third_two_plate.get_top(),
            color = BLACK,
        )
        arrow_second_two_to_third_three = Arrow(
            start = second_two_plate.get_left(),
            end = third_three_plate.get_top(),
            color = BLACK,
        )
        arrow_second_two_to_third_fourth = Arrow(
            start = second_two_plate.get_right(),
            end = third_four_plate.get_top(),
            color = BLACK,
        )
        # Arrows from third to fourth iteration
        arrow_second_zero_to_left = Arrow(
            start=third_one_plate.get_left(),
            end=third_one_plate.get_center() + DOWN * 1 + LEFT * 1,  # Position for next plate
            color=BLACK,
        )
        arrow_second_zero_to_right = Arrow(
            start=third_one_plate.get_right(),
            end=third_one_plate.get_center() + DOWN * 1 + RIGHT * 1,  # Position for next plate
            color=BLACK,
        )
        arrow_second_first_to_left = Arrow(
            start=third_two_plate.get_left(),
            end=third_two_plate.get_center() + DOWN * 1 + LEFT * 1,
            color=BLACK,
        )
        arrow_second_first_to_right = Arrow(
            start=third_two_plate.get_right(),
            end=third_two_plate.get_center() + DOWN * 1 + RIGHT * 1,
            color=BLACK,
        )
        arrow_second_second_to_left = Arrow(
            start=third_three_plate.get_left(),
            end=third_three_plate.get_center() + DOWN * 1 + LEFT * 1,
            color=BLACK,
        )
        arrow_second_second_to_right = Arrow(
            start=third_three_plate.get_right(),
            end=third_three_plate.get_center() + DOWN * 1 + RIGHT * 1,
            color=BLACK,
        )
        arrow_second_third_to_left = Arrow(
            start=third_four_plate.get_left(),
            end=third_four_plate.get_center() + DOWN * 1 + LEFT * 1,
            color=BLACK,
        )
        arrow_second_third_to_right = Arrow(
            start=third_four_plate.get_right(),
            end=third_four_plate.get_center() + DOWN * 1 + RIGHT * 1,
            color=BLACK,
        )
        dots = Tex("......", color=BLACK, font_size = 30 ).next_to(
            arrow_second_zero_to_left.get_end(), DOWN, buff=0.5
        )

       

        # Animation
        # Schrift
        self.add(beispiel_text, formula)
        self.wait(1)

        # First Iteration
        self.add(first_plate)
        self.add(label_first_plate)
        self.wait(1)
        self.add(arrow_first_to_second_one)
        self.add(arrow_first_to_second_two)
        self.wait(1)

        # Second Iteration
        self.add(second_one_plate)
        self.add(second_two_plate)
        self.add(label_second_iteration)
        self.wait(1)
        self.add(arrow_second_one_to_third_one)
        self.add(arrow_second_one_to_third_two)
        self.add(arrow_second_two_to_third_three)
        self.add(arrow_second_two_to_third_fourth)
        self.wait(1)

        # Third Iteration
        self.add(third_one_plate)
        self.add(third_two_plate)
        self.add(third_three_plate)
        self.add(third_four_plate)
        self.add(label_third_iteration)
        self.wait(1)
        self.add(arrow_second_zero_to_left)
        self.add(arrow_second_zero_to_right)
        self.add(arrow_second_first_to_left)
        self.add(arrow_second_first_to_right)
        self.add(arrow_second_second_to_left)
        self.add(arrow_second_second_to_right)
        self.add(arrow_second_third_to_left)
        self.add(arrow_second_third_to_right)
        self.wait(1)
        self.add(dots)
        self.wait(1)
