from manim import *

class Mittelwertsatz(Scene):
    def construct(self):
        text1 = Text("Mittelwertsatz der Integralrechnung", font_size=36, color=YELLOW)

        equation = MathTex(
            r"\int_a^b f(x) \, dx = f(\xi)(b - a)",
            font_size=36, color=WHITE
        ).next_to(text1, DOWN, buff=0.5)

        # Create a NumberPlane with tips
        plane = NumberPlane(
            x_range=[-2, 10, 1],
            y_range=[-1, 5, 1],
            x_length=11,
            y_length=7,
            axis_config={"include_tip": True},  # Add tips to axes
            background_line_style={
                "stroke_color": BLUE_D,
                "stroke_width": 1,
                "stroke_opacity": 0.6,
            },
        )

        # Add labels to axes for clarity
        plane_labels = plane.get_axis_labels(x_label="x", y_label="f(x)")

        # Define the curve
        function = lambda x: 0.1 * (x - 3) ** 3 + 1

        # Create a graph of the function using ParametricFunction
        graph = ParametricFunction(
            lambda t: plane.c2p(t, function(t)),  # Map function to the plane
            t_range=[0, 6.5],
            color=BLUE
        )

        # Interval [a, b]
        a = 2
        b = 6

        # Adding 'a' and 'b' at the x-axis
        a_label = MathTex("a").next_to(plane.c2p(a, 0), DOWN, buff=0.2)
        b_label = MathTex("b").next_to(plane.c2p(b, 0), DOWN, buff=0.2)

        # Fill area under the curve
        filled_area = plane.get_area(
            graph, x_range=[a, b], color=GREEN, opacity=0.5
        )

        # Label for the integral ∫_a^b f(x) dx
        integral_label = MathTex(
            r"\int_a^b f(x) \, dx", 
            color=YELLOW
        ).scale(0.8).move_to(plane.c2p(8, 2.5))  # Position above the filled area

        # Arrow from the filled area to the integral label
        arrow_integral_label = Arrow(
            start=plane.c2p(5.5, 2),  
            end=plane.c2p(7, 2.5),               
            buff=0.2,
            color=YELLOW
        )

        # ValueTracker for moving xi
        xi_tracker = ValueTracker(4.4)

        # Dynamic dot at xi
        xi_dot = always_redraw(lambda: Dot(
            plane.c2p(xi_tracker.get_value(), function(xi_tracker.get_value())),
            color=RED
        ))

        # Dynamic vertical line at xi
        xi_line = always_redraw(lambda: plane.get_vertical_line(
            plane.c2p(xi_tracker.get_value(), function(xi_tracker.get_value())),
            color=WHITE
        ))

        # Dynamic label for xi
        xi_label = always_redraw(lambda: MathTex(r"\xi").next_to(
            plane.c2p(xi_tracker.get_value(), 0), DOWN, buff=0.2
        ))

        # Dynamic horizontal line at f(xi)
        f_xi_line = always_redraw(lambda: plane.get_horizontal_line(
            plane.c2p(xi_tracker.get_value(), function(xi_tracker.get_value())),
            color=WHITE
        ))

        # Dynamic label for f(xi)
        f_xi_label = always_redraw(lambda: MathTex(r"f(\xi)").next_to(
            plane.c2p(0, function(xi_tracker.get_value())), LEFT, buff=0.2
        ))

        # Dynamic rectangle with the bottom edge aligned to the x-axis
        rectangle = always_redraw(lambda: Rectangle(
            width=plane.c2p(b, 0)[0] - plane.c2p(a, 0)[0],  # Width: b - a
            height=function(xi_tracker.get_value() + 0.2),  # Height at f(ξ) + 0.2 for better visibility
            color=BLUE,
            fill_opacity=0.5,
        ).move_to(plane.c2p((a + b) / 2, function(xi_tracker.get_value()) / 2 - 0.03)))  

        # Label for the rectangle: f(ξ)(b-a) = ∫_a^b f(x) dx
        rectangle_label = MathTex(
            r"f(\xi)(b-a) = \int_a^b f(x) \, dx", 
            color=YELLOW
        ).scale(0.8).move_to(plane.c2p((a + b) / 2, -1))  

        # Arrow from the top of the rectangle to the rectangle label
        arrow_rectangle_label = Arrow(
            start=plane.c2p((a + b) / 2, 1),  # Top-center of the rectangle
            end=rectangle_label.get_center(),  # Point to the label
            buff=0.2,
            color=YELLOW
        )

        # Add basic elements to the scene
        self.play(Write(text1), run_time=2)
        self.play(Write(equation), run_time=3)
        self.wait(2)
        self.play(FadeOut(text1), FadeOut(equation), run_time=2)
        self.play(Create(plane), Write(plane_labels), run_time=3)
        self.play(Create(graph), run_time=3)
        self.wait(2)

        # Add 'a' and 'b' labels
        self.play(Write(a_label), Write(b_label), run_time=2)
        self.play(FadeIn(filled_area), run_time=3)
        self.play(Create(arrow_integral_label), run_time=2)
        self.play(Write(integral_label), run_time=3)

        # Add rectangle, lines, labels, and dot
        self.play(
            Create(rectangle), 
            Create(xi_line), 
            Create(f_xi_line),
            Create(xi_dot),
            Write(xi_label),
            Write(f_xi_label),
            run_time=3
        )

        # Animate the movement of xi
        self.play(xi_tracker.animate.set_value(5), run_time=6, rate_func=linear)
        self.wait(2)
        self.play(xi_tracker.animate.set_value(4.5), run_time=6, rate_func=linear)
        self.wait(2)
        self.play(xi_tracker.animate.set_value(4.8), run_time=4, rate_func=smooth)
        self.play(Create(arrow_rectangle_label), run_time=2)
        self.play(Write(rectangle_label), run_time=3)
        self.wait(4)
