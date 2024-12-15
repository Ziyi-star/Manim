from manim import *

class Mittelwertsatz(Scene):
    def construct(self):
        # Background grid
        grid = NumberPlane(
            background_line_style={
                "stroke_color": BLUE_D,
                "stroke_width": 1,
                "stroke_opacity": 0.6,
            },
            axis_config={
                "stroke_color": BLUE_D,
                "stroke_width": 1,
                "stroke_opacity": 0.6,
            },
        )

        # Axes
        ax = Axes(
            x_range=[-1, 10, 1],
            y_range=[-1, 5, 1],
            x_length=11,
            y_length=7,
            axis_config={"color": WHITE},
            tips=True,
        ).to_edge(UP)

        # Labels
        x_label = ax.get_x_axis_label(Tex("x").scale(0.7))
        y_label = ax.get_y_axis_label(Tex("f(x)").scale(0.7))

        # Define the curve
        f = lambda x: 0.1 * (x - 3)**3 + 1
        curve = ax.plot(f, color=BLUE, x_range=[0, 6.5])

        # Interval [a, b]
        a = 2
        b = 6

        # Adding 'a' and 'b' at the x-axis
        a_label = MathTex("a").next_to(ax.c2p(a, 0), DOWN, buff=0.2)  # Label at x = a
        b_label = MathTex("b").next_to(ax.c2p(b, 0), DOWN, buff=0.2)  # Label at x = b

        # Filled area under the curve
        filled_area = ax.get_area(
            graph=curve,
            x_range=[a, b],
            color=GREEN,
            opacity=0.6
        )

        # Label for the integral ∫_a^b f(x) dx
        integral_label = MathTex(
            r"\int_a^b f(x) \, dx", 
            color=YELLOW
        ).scale(0.8).move_to(ax.c2p(8, 2.5))  # Position above the filled area

        # Arrow from the filled area to the integral label
        arrow_integral_label = Arrow(
            start=ax.c2p(5.5,2),  
            end=ax.c2p(7, 2.5),               
            buff=0.2,
            color=YELLOW
        )

        # ValueTracker for moving xi
        xi_tracker = ValueTracker(4.4)

        # Dynamic dot at xi
        xi_dot = always_redraw(lambda: Dot(
            ax.c2p(xi_tracker.get_value(), f(xi_tracker.get_value())),
            color=RED
        ))

        # Dynamic rectangle with the bottom edge aligned to the x-axis
        rectangle = always_redraw(lambda: Rectangle(
            # Width: b - a
            width=ax.c2p(b, 0)[0] - ax.c2p(a, 0)[0],  
            # Height at f(ξ) + 0.2 for better visibility
            height=f(xi_tracker.get_value())+0.2,         
            color=BLUE,
            fill_opacity=0.5,
            # Align bottom edge at y=0 (x-axis)
        ).move_to(ax.c2p((a + b) / 2, 0), DOWN))  

        # Label for the rectangle: f(si)(b-a) = ∫_a^b f(x) dx
        rectangle_label = MathTex(
            r"f(\xi)(b-a) = \int_a^b f(x) \, dx", 
            color=YELLOW
        ).scale(0.8).move_to(ax.c2p((a + b) / 2, -1))  # Position below the filled area

        # Arrow from the top of the rectangle to the rectangle label
        arrow_rectangle_label = Arrow(
                start=ax.c2p((a + b) / 2, 0.8),  # Dynamic top-center of the rectangle
                end=rectangle_label.get_center(),                    # Point to the label
                buff=0.2,
                color=YELLOW
            )



        # Dynamic vertical line at xi
        xi_line = always_redraw(lambda: ax.get_vertical_line(
            ax.c2p(xi_tracker.get_value(), f(xi_tracker.get_value())),
            color=BLACK
        ))

        # Add basic elements to the scene
        self.play(Create(grid))
        self.play(Create(ax))
        self.play(Write(x_label), Write(y_label))
        self.play(Create(curve), run_time=2)

        # Add 'a' and 'b' to the scene
        self.play(Write(a_label), Write(b_label))
        self.play(FadeIn(filled_area))

        # Add the arrow pointing to the integral label
        self.play(Create(arrow_integral_label))
        
        # Add the integral label to the area
        self.play(Write(integral_label))

        # Add the dynamic rectangle elements
        self.play(Create(rectangle), Create(xi_line), Create(xi_dot))

        # Add the rectangle label
        self.play(Create(arrow_rectangle_label))
        self.play(Write(rectangle_label))
        

        # si move animation
        # 1. Move xi_dot and rectangle from xi = 4.4 to 5
        self.play(xi_tracker.animate.set_value(5), run_time=3, rate_func=linear)
        self.wait(1)

        # 2. Move xi_dot and rectangle back from xi = 4.9 to 4.5
        self.play(xi_tracker.animate.set_value(4.5), run_time=3, rate_func=linear)
        self.wait(1)

        # 3. Move to the final point at xi = 4.8
        self.play(xi_tracker.animate.set_value(4.8), run_time=2, rate_func=smooth)
        self.wait(2)
