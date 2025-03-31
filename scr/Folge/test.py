import random
from manim import *

config.background_color = WHITE

class FolgenRekursionHorizontalTest(Scene):
    def create_plate_with_dot(self, position=ORIGIN, stored_blob_points=None):
        """Creates a plate with nested circles and a blob."""
        plate = VGroup(
            Circle(radius=0.3, color=BLACK, fill_color=WHITE, fill_opacity=1, stroke_width=4),
            Circle(radius=0.2, color=BLACK, fill_color=BLUE_B, fill_opacity=1, stroke_width=2)
        ).move_to(position)
        
        blob = self.create_blob(stored_blob_points)
        blob.move_to(plate[1].get_center())
        plate.add(blob)
        return plate
    
    def create_blob(self, stored_points=None):
        """Creates or reuses a blob shape."""
        blob = VMobject(color=BLACK, fill_opacity=1)
        if stored_points is not None:
            blob.set_points(stored_points)
            return blob
            
        points = []
        for i in range(8):
            angle = i * TAU / 8
            offset = random.uniform(0.7, 1.3)
            x, y = 0.05 * np.cos(angle) * offset, 0.05 * np.sin(angle) * offset
            points.append([x, y, 0])
        points.append(points[0])
        blob.set_points_smoothly(points)
        return blob

    def create_arrow(self, start_mob, end_mob, direction="", buff=0.2):
        start = start_mob.get_right() if direction == "right" else start_mob.get_left()
        
        # Fix: Handle end position correctly
        if direction == "":
            end = end_mob.get_top()
        else:
            # Create direction vector based on string
            dir_vector = LEFT if direction == "left" else RIGHT
            end = end_mob.get_center() + DOWN + dir_vector

        return Arrow(start=start, end=end, color=BLACK, buff=buff)

    def create_dots(self, position, buff=0.5):
        """Creates dots for continuation."""
        return Tex("......", color=BLACK, font_size=30).next_to(position, buff=buff)

    def construct(self):
        # Store blob points for reuse
        stored_blob = self.create_blob()
        stored_points = stored_blob.get_points()

        # First level
        zero_plate = self.create_plate_with_dot(UP * 3, stored_points)
        self.add(zero_plate)
        self.wait(1)

        # Second level
        second_positions = [
            zero_plate.get_center() + DOWN * 1 + LEFT * 2,
            zero_plate.get_center() + DOWN * 1 + RIGHT * 2
        ]
        second_plates = [self.create_plate_with_dot(pos, stored_points) for pos in second_positions]
        arrows_second = [
            self.create_arrow(zero_plate, plate, "right" if i else "left")
            for i, plate in enumerate(second_plates)
        ]

        self.add(*second_plates)
        self.wait(1)
        self.add(*arrows_second)
        self.wait(1)

        # Third level - similar pattern continues...
        # ...existing code for remaining levels...