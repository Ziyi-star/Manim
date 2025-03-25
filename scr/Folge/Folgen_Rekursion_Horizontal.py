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
                radius=0.7,
                color=BLACK,
                fill_color=WHITE,
                fill_opacity=1,
                stroke_width=4,  # Thicker border for plate edge
            ).move_to(position)

            # Create inner circle
            inner_circle = Circle(
                radius=0.5,
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
                radius = 0.1
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
        zero_plate = create_plate_with_dot(position=5 * LEFT)
        # # Create label
        # label = MathTex("a_1 = 1", color=BLACK)
        # label.next_to(zero_plate, UP, buff=0.3)
            
        # Second iteration
        first_up_plate = create_plate_with_dot(
            position=zero_plate.get_center() + UP * 2 + RIGHT * 2.5
        )
        first_down_plate = create_plate_with_dot(
            position=zero_plate.get_center() + DOWN * 2 + RIGHT * 2.5
        )
        # Arrows
        arrow_zero_to_up = Arrow(
            start=zero_plate.get_corner(UR),
            end=first_up_plate.get_left(),
            color=BLACK,
        )
        arrow_zero_to_down = Arrow(
            start=zero_plate.get_corner(DR), 
            end=first_down_plate.get_left(),
            color=BLACK,
        )
        
        # Third iteration
        second_zero_plate = create_plate_with_dot(
            position=first_up_plate.get_center() + UP * 1 + RIGHT * 2.5
        )
        second_first_plate = create_plate_with_dot(
            position=first_up_plate.get_center() + DOWN * 1 + RIGHT * 2.5
        )
        second_second_plate = create_plate_with_dot(
            position=first_down_plate.get_center() + UP * 1 + RIGHT * 2.5
        )
        second_third_plate = create_plate_with_dot(
            position=first_down_plate.get_center() + DOWN * 1 + RIGHT * 2.5
        )
        arrow_first_up_to_second_zero = Arrow(
            start = first_up_plate.get_right(),
            end = second_zero_plate.get_left(),
            color = BLACK,
        )
        arrow_first_up_to_second_first = Arrow(
            start = first_up_plate.get_right(),
            end = second_first_plate.get_left(),
            color = BLACK,
        )
        arrow_first_down_to_second_second = Arrow(
            start = first_down_plate.get_right(),
            end = second_second_plate.get_left(),
            color = BLACK,
        )
        arrow_first_down_to_second_third = Arrow(
            start = first_down_plate.get_right(),
            end = second_third_plate.get_left(),
            color = BLACK,
        )

        # Animation
        # 1. Spalte
        self.add(zero_plate)
        #self.add(label)

        # 2. Spalte
        self.add(first_up_plate)
        self.add(first_down_plate)
        self.wait(1)
        self.add(arrow_zero_to_up)
        self.add(arrow_zero_to_down)
        self.wait(1)

        # 3. Spalte
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
