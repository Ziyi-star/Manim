import random
from manim import *

config.background_color = WHITE


class FolgenRekursionHorizontal(Scene):
    def construct(self):
        # Store the first blob's points
        stored_blob_points = None
        
        def create_plate_with_dot(position=ORIGIN):
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

        # Create main plate
        zero_plate = create_plate_with_dot(position=UP*3)
        # # Create label
        # label = MathTex("a_1 = 1", color=BLACK)
        # label.next_to(zero_plate, UP, buff=0.3)
            
        # Second iteration
        first_left_plate = create_plate_with_dot(
            position=zero_plate.get_center() + DOWN * 1 + LEFT * 2
        )
        first_right_plate = create_plate_with_dot(
            position=zero_plate.get_center() + DOWN * 1 + RIGHT * 2
        )
        # Arrows
        arrow_zero_to_left = Arrow(
            start=zero_plate.get_left(),
            end=first_left_plate.get_top(),
            color=BLACK,
        )
        arrow_zero_to_right = Arrow(
            start=zero_plate.get_right(), 
            end=first_right_plate.get_top(),
            color=BLACK,
        )
        
        # Third iteration
        second_zero_plate = create_plate_with_dot(
            position=first_left_plate.get_center() + DOWN * 1 + LEFT * 1
        )
        second_first_plate = create_plate_with_dot(
            position=first_left_plate.get_center() + DOWN * 1 + RIGHT * 1
        )
        second_second_plate = create_plate_with_dot(
            position=first_right_plate.get_center() + DOWN * 1 + LEFT * 1
        )
        second_third_plate = create_plate_with_dot(
            position=first_right_plate.get_center() + DOWN * 1 + RIGHT * 1
        )
        arrow_first_up_to_second_zero = Arrow(
            start = first_left_plate.get_left(),
            end = second_zero_plate.get_top(),
            color = BLACK,
        )
        arrow_first_up_to_second_first = Arrow(
            start = first_left_plate.get_right(),
            end = second_first_plate.get_top(),
            color = BLACK,
        )
        arrow_first_down_to_second_second = Arrow(
            start = first_right_plate.get_left(),
            end = second_second_plate.get_top(),
            color = BLACK,
        )
        arrow_first_down_to_second_third = Arrow(
            start = first_right_plate.get_right(),
            end = second_third_plate.get_top(),
            color = BLACK,
        )

        # Fourth Arrows
        arrow_second_zero_to_left = Arrow(
            start=second_zero_plate.get_left(),
            end=second_zero_plate.get_center() + DOWN * 1 + LEFT * 1,  # Position for next plate
            color=BLACK,
        )
        arrow_second_zero_to_right = Arrow(
            start=second_zero_plate.get_right(),
            end=second_zero_plate.get_center() + DOWN * 1 + RIGHT * 1,  # Position for next plate
            color=BLACK,
        )
        arrow_second_first_to_left = Arrow(
            start=second_first_plate.get_left(),
            end=second_first_plate.get_center() + DOWN * 1 + LEFT * 1,
            color=BLACK,
        )
        arrow_second_first_to_right = Arrow(
            start=second_first_plate.get_right(),
            end=second_first_plate.get_center() + DOWN * 1 + RIGHT * 1,
            color=BLACK,
        )
        arrow_second_second_to_left = Arrow(
            start=second_second_plate.get_left(),
            end=second_second_plate.get_center() + DOWN * 1 + LEFT * 1,
            color=BLACK,
        )
        arrow_second_second_to_right = Arrow(
            start=second_second_plate.get_right(),
            end=second_second_plate.get_center() + DOWN * 1 + RIGHT * 1,
            color=BLACK,
        )
        arrow_second_third_to_left = Arrow(
            start=second_third_plate.get_left(),
            end=second_third_plate.get_center() + DOWN * 1 + LEFT * 1,
            color=BLACK,
        )
        arrow_second_third_to_right = Arrow(
            start=second_third_plate.get_right(),
            end=second_third_plate.get_center() + DOWN * 1 + RIGHT * 1,
            color=BLACK,
        )
        dots = Tex("......", color=BLACK, font_size = 30 ).next_to(
            arrow_second_zero_to_left.get_end(), DOWN, buff=0.5
        )

        #Fifth iteration
        third_zero_plate = create_plate_with_dot(
            position=dots.get_center() + DOWN * 1 + LEFT * 0.5
        )
        dots_at_fifth_zero = Tex("......", color=BLACK, font_size = 30 ).next_to(
            third_zero_plate.get_center(), RIGHT, buff=0.5
        )

        third_first_plate = create_plate_with_dot(
            position=dots_at_fifth_zero.get_center() + RIGHT * 1
        )
        dots_at_fifth_first = Tex("......", color=BLACK, font_size = 30 ).next_to(
            third_first_plate.get_center(), RIGHT, buff=0.5
        )

        third_second_plate = create_plate_with_dot(
            position=dots_at_fifth_first.get_center() + RIGHT * 1
        )
        dots_at_fifth_second = Tex("......", color=BLACK, font_size = 30 ).next_to(
            third_second_plate.get_center(), RIGHT, buff=0.5
        )

        third_third_plate = create_plate_with_dot(
            position=dots_at_fifth_second.get_center() + RIGHT * 1
        )
        dots_at_fifth_third = Tex("......", color=BLACK, font_size = 30 ).next_to(
            third_third_plate.get_center(), RIGHT, buff=0.5
        )

        third_fourth_plate = create_plate_with_dot(
            position=dots_at_fifth_third.get_center() + RIGHT * 1
        )
        dots_at_fifth_fourth = Tex("......", color=BLACK, font_size = 30 ).next_to(
            third_fourth_plate.get_center(), RIGHT, buff=0.5
        )
        third_fifth_plate = create_plate_with_dot(
            position=dots_at_fifth_fourth.get_center() + RIGHT * 1
        )

        # Animation
        # 1. Zeile
        self.add(zero_plate)
        #self.add(label)
        self.wait(1)

        # 2. Zeile
        self.add(first_left_plate)
        self.add(first_right_plate)
        self.wait(1)
        self.add(arrow_zero_to_left)
        self.add(arrow_zero_to_right)
        self.wait(1)

        # 3. Zeile
        self.add(second_zero_plate)
        self.add(second_first_plate)
        self.add(second_second_plate)
        self.add(second_third_plate)
        self.wait(1)
        self.add(arrow_first_up_to_second_zero)
        self.add(arrow_first_up_to_second_first)
        self.add(arrow_first_down_to_second_second)
        self.add(arrow_first_down_to_second_third)
        self.wait(1)

        # 4. Zeile arrows
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

        # 5. Zeile
        self.add(third_zero_plate)
        self.add(dots_at_fifth_zero)
        self.add(third_first_plate)
        self.add(dots_at_fifth_first)
        self.add(third_second_plate)
        self.add(dots_at_fifth_second)
        self.add(third_third_plate)
        self.add(dots_at_fifth_third)
        self.add(third_fourth_plate)
        self.add(dots_at_fifth_fourth)
        self.add(third_fifth_plate)
        self.wait(1)
