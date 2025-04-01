import random
from manim import *

config.background_color = WHITE

'''
Name convention:
Circle from first iteration is called first plate.
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
        first_plate = create_plate_with_blob(position=UP*2.5 + RIGHT*2.5)
        # label for first plate
        label_first_plate = MathTex(
            "a_{", "1", "} = ", "2", "= ", "2", "^{", "1", "}",
            color=BLACK
        ).to_edge(LEFT, buff=0.5).shift(
            UP * first_plate.get_center()[1]
        )
        # Color the indices in red and base in blue
        label_first_plate[1].set_color(RED)    # First "1" (index)
        label_first_plate[7].set_color(RED)    

        # Second iteration Circles
        second_one_plate = create_plate_with_blob(
            position=first_plate.get_center() + DOWN * 1 + LEFT * 2
        )
        second_two_plate = create_plate_with_blob(
            position=first_plate.get_center() + DOWN * 1 + RIGHT * 2
        )
        label_second_iteration = MathTex("a_{", "2", "} = ", "2", "a_{", "1", "} = ", "2", "^{", "2", "}", color=BLACK).to_edge(LEFT, buff=0.5).shift(UP * second_one_plate.get_center()[1])
        label_second_iteration[1].set_color(RED)
        label_second_iteration[9].set_color(RED)        

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
        label_third_iteration = MathTex("a_{", "3", "} = ", "2", "a_{", "2", "} = ", "2", "^{", "3", "}", color=BLACK).to_edge(LEFT, buff=0.5).shift(UP * third_one_plate.get_center()[1])
        label_third_iteration[1].set_color(RED)    
        label_third_iteration[9].set_color(RED)
        
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

        fourth_iteration_positions = [
            third_one_plate.get_center() + DOWN * 1 + LEFT * 0.5,    # Increased horizontal spacing
            third_one_plate.get_center() + DOWN * 1 + RIGHT * 0.5,
            third_two_plate.get_center() + DOWN * 1 + LEFT * 0.5,
            third_two_plate.get_center() + DOWN * 1 + RIGHT * 0.5,
            third_three_plate.get_center() + DOWN * 1 + LEFT * 0.5,
            third_three_plate.get_center() + DOWN * 1 + RIGHT * 0.5,
            third_four_plate.get_center() + DOWN * 1 + LEFT * 0.5,
            third_four_plate.get_center() + DOWN * 1 + RIGHT * 0.5,
        ]
        fourth_iteration_plates = [
            create_plate_with_blob(pos) for pos in fourth_iteration_positions
        ]

        # Create arrows from third to fourth iteration
        third_plates = [third_one_plate, third_two_plate, third_three_plate, third_four_plate]
        third_to_fourth_arrows = []

        for i, plate in enumerate(third_plates):
            # Create left arrow to corresponding fourth iteration plate
            left_arrow = Arrow(
                start=plate.get_left(),
                end=fourth_iteration_plates[i*2].get_top(),  # Connect to corresponding fourth plate
                color=BLACK,
            )
            # Create right arrow to next fourth iteration plate
            right_arrow = Arrow(
                start=plate.get_right(),
                end=fourth_iteration_plates[i*2+1].get_top(),  # Connect to next fourth plate
                color=BLACK,
            )
            third_to_fourth_arrows.extend([left_arrow, right_arrow])

        label_fourth_iteration = MathTex("a_{", "4", "} = ", "2", "a_{", "3", "} = ", "2", "^{", "4", "}", color=BLACK).to_edge(LEFT, buff=0.5).shift(UP * fourth_iteration_plates[0 ].get_center()[1])
        label_fourth_iteration[1].set_color(RED)
        label_fourth_iteration[9].set_color(RED)
        # After label_fourth_iteration definition, add:
        vertical_dots_one = Tex("\\vdots", color=BLACK, font_size=40).next_to(
            label_fourth_iteration, 
            DOWN,
            buff=0.5
        )

        # Create arrows for fourth iteration plates
        fourth_iteration_arrows = []
        for plate in fourth_iteration_plates:
            # Create left arrow
            left_arrow = Arrow(
                start=plate.get_left(),
                end=plate.get_center() + DOWN * 1 + LEFT * 0.5,
                color=BLACK,
            )
            # Create right arrow
            right_arrow = Arrow(
                start=plate.get_right(),
                end=plate.get_center() + DOWN * 1 + RIGHT * 0.5,
                color=BLACK,
            )
            fourth_iteration_arrows.extend([left_arrow, right_arrow])
        
        # Add three sets of vertical dots under fourth iteration arrows
        fourth_iteration_vertical_dots = []
        for i in range(3):
            dots = Tex("\\vdots", color=BLACK, font_size=30).next_to(
                fourth_iteration_arrows[i*7].get_end(), 
                DOWN,
                buff=0.3
            )
            fourth_iteration_vertical_dots.append(dots)
    

        # n iteration
        # positions for n iteration plates (5 plates evenly distributed)
        left_pos = fourth_iteration_plates[0].get_center() + DOWN * 2 + LEFT * 0.5
        right_pos = fourth_iteration_plates[7].get_center() + DOWN * 2 + RIGHT * 0.5

        # Calculate horizontal spacing between plates
        total_distance = abs(right_pos[0] - left_pos[0])  # X-axis distance
        spacing = total_distance / 4  # For 5 plates, we need 4 intervals

        n_iteration_positions = [
            np.array([left_pos[0] + i * spacing, left_pos[1], left_pos[2]]) 
            for i in range(5)
        ]
        # plates
        n_iteration_plates = [
            create_plate_with_blob(pos) for pos in n_iteration_positions
        ]
        #label
        label_n_iteration = MathTex("a_{", "n", "} = ", "2", "a_{", "n-1", "} = ", "2", "^{", "n", "}",color=BLACK).to_edge(LEFT, buff=0.5).shift(UP * n_iteration_plates[0].get_center()[1])
        label_n_iteration[1].set_color(RED)    
        label_n_iteration[9].set_color(RED)
        
        #dots
        n_iteration_dots = []
        for i in range(4):
            dots = Tex("......", color=BLACK, font_size=30).next_to(
                n_iteration_plates[i].get_center(), RIGHT, buff=0.8
            )
            n_iteration_dots.append(dots)

        # n+1 iteration
        # plates
        n_plus_1_iteration_positions = []
        for plate in n_iteration_plates:
            # Create positions for left and right child plates
            left_pos = plate.get_center() + DOWN * 1 + LEFT * 0.4
            right_pos = plate.get_center() + DOWN * 1 + RIGHT * 0.4
            n_plus_1_iteration_positions.extend([left_pos, right_pos])
        n_plus_1_iteration_plates = [
            create_plate_with_blob(pos) for pos in n_plus_1_iteration_positions
        ]
        #dots
        n_plus_1_iteration_dots = []
        for i in range(1,8,2):
            dots = Tex("...", color=BLACK, font_size=30).next_to(
                n_plus_1_iteration_plates[i].get_right(), RIGHT
            )
            n_plus_1_iteration_dots.append(dots)
        #label
        label_n_plus_1_iteration = MathTex("a_{", "n+1", "} = ", "2", "a_{", "n", "} = ", "2", "^{", "n+1", "}", color=BLACK).to_edge(LEFT, buff=0.5).shift(UP * n_plus_1_iteration_plates[0].get_center()[1])
        label_n_plus_1_iteration[1].set_color(RED)
        label_n_plus_1_iteration[9].set_color(RED)

        # Arrows from n to n+1 iteration
        n_to_n_plus_1_arrows = []
        for i, plate in enumerate(n_iteration_plates):
            # Create left arrow
            left_arrow = Arrow(
                start=plate.get_left(),
                end=n_plus_1_iteration_plates[i*2].get_top(),
                color=BLACK,
            )
            # Create right arrow
            right_arrow = Arrow(
                start=plate.get_right(),
                end=n_plus_1_iteration_plates[i*2+1].get_top(),
                color=BLACK,
            )
            n_to_n_plus_1_arrows.extend([left_arrow, right_arrow])


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
        self.add(*third_to_fourth_arrows)
        self.wait(1)

        # Fourth Iteration
        self.add(*fourth_iteration_plates)
        self.add(label_fourth_iteration)
        self.wait(1)
        self.add(*fourth_iteration_arrows)
        self.wait(1)
        self.add(vertical_dots_one)
        self.add(*fourth_iteration_vertical_dots)
        self.wait(1)

        # n iteration 
        self.add(*n_iteration_plates)
        self.add(*n_iteration_dots)
        self.add(label_n_iteration)
        self.wait(1)

        # n plus 1 iteration_plates:
        self.add(*n_plus_1_iteration_plates)
        self.add(*n_plus_1_iteration_dots)
        self.add(label_n_plus_1_iteration)
        self.add(*n_to_n_plus_1_arrows)
        self.wait(1)


