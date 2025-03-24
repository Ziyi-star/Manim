import cv2
import numpy as np
from manim import *

class TraceImage(Scene):
    def construct(self):
        # Load image using OpenCV
        image_path = "FolgeParabel.jpeg"  # Change this to your image file
        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Convert to grayscale
        img = cv2.resize(img, (600, 400))  # Resize for better performance

        # Edge detection using Canny
        edges = cv2.Canny(img, threshold1=50, threshold2=150)

        # Find contours
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        traced_objects = []
        for contour in contours:
            points = [np.array([x / 100 - 3, -y / 100 + 2, 0]) for x, y in contour[:, 0, :]]
            if len(points) > 2:
                traced_path = VMobject()
                traced_path.set_points_smoothly(points)
                traced_path.set_stroke(WHITE, width=1)
                traced_objects.append(traced_path)

        # Draw all contours
        self.play(*[Create(obj) for obj in traced_objects], run_time=3)
        self.wait(2)
