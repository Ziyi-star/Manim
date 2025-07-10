from manim import *
from matplotlib import axes, table

class NullstellenRekursion(Scene):
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
        # Funktion Animation
        # Create axes for the graph on the right
        axes = Axes(
            x_range=[-3.5, 3.5, 1],
            y_range=[-23, 23, 5],
            y_length=10,
            x_length=12,
            axis_config={"include_numbers": True, "font_size": 24}
        ).scale(0.75).to_edge(LEFT, buff=5)
        # Define a function for the graph
        def func(x):
            return x**3 - 2*x + 2

        # Plot the function
        graph = axes.plot(func, x_range=[-3, 3], color=BLUE)
        label_graph = axes.get_graph_label(
            graph, 
            label="f(x)", 
            x_val=3.2,  # Position where label appears
            direction=LEFT * 1.5,
            color=BLUE
        ).scale(0.6)

         # Table Data (same as in your image)
        table_data = [
            ["0", "-2.5000", "-8.6250"],
            ["1", "-1.9851", "-1.8521"],
            ["2", "-1.7965", "-0.2051"],
            ["3", "-1.7698", "-0.0038"],
            ["4", "-1.7693", "-0.0000"],
            ["5", "-1.7693", "-0.0000"],
            ["6", "-1.769292", "0.0000"],
            ["7", "-1.769292", "0.0000"],
        ]

        # Create Table
        table = Table(
            table_data,
            col_labels=[
                Text("Iteration", font_size=40),
                MathTex(r"\mathbf{x_n}", font_size=60),
                MathTex(r"\mathbf{f(x_n)}", font_size=60)
            ],
            top_left_entry=Text(""),
            include_outer_lines=True,
            line_config={"stroke_width": 3},

        ).scale(0.4).to_edge(LEFT, buff=0.2)
        # Make table entries invisible (but keep headers visible)
        for entry in table.get_entries():
            entry.set_opacity(0)
        # Ensure column labels are visible
        for label in table.get_col_labels():
            label.set_opacity(1)
        title = MathTex(
            r"\text{Newton Iteration }(x_0 = -2.5)",
            color=WHITE
        ).scale(0.8).next_to(table, UP, buff=0.5).align_to(table, LEFT)

        def create_point_elements(x_val, fx_val, index):
            # Create point on function
            point = Dot(
                axes.c2p(x_val, fx_val),
                color=GREEN,
                radius=0.05
            )
            # Create x-axis marker and label
            cross = MathTex(
                r"\mathbf{X}",
                color=GREEN
            ).scale(0.6).move_to(axes.c2p(x_val, 0))
            label = MathTex(
                f"x_{index}",
                color=GREEN
            ).scale(0.6).next_to(cross, UP, buff=0.2)
            
            # Create dashed vertical line
            vertical_line = DashedLine(
                end=axes.c2p(x_val, fx_val),
                start=axes.c2p(x_val, 0),
                color=GREEN
            )
            return point, cross, label, vertical_line

        # Animation
        self.add(grid,axes)
        self.play(Create(graph), run_time=2)
        self.play(Write(label_graph), run_time=1.5)
        self.wait(1.5)
        # Show the table
        self.add(title)
        self.play(FadeIn(table), run_time=2)
        self.wait(1.5)
        # 1. Scene
        x0_val = float(table_data[0][1]) 
        fx0_val = float(table_data[0][2]) 
        x0_index = table.get_entries()[3]   # Second row, first column
        x0_cell = table.get_entries()[4] 
        fx0_val_cell = table.get_entries()[5]
        point_on_graph, x0_cross, x0_label, x0_vertical_line = create_point_elements(
            x0_val, fx0_val, 0
        )  
        self.play(x0_index.animate.set_opacity(1), run_time=1)
        self.play(x0_cell.animate.set_opacity(1), run_time=1)
        self.play(Create(x0_cross), run_time=1)
        self.play(Write(x0_label), run_time=1)
        self.play(fx0_val_cell.animate.set_opacity(1), run_time=1)
        self.play(Create(x0_vertical_line), run_time=1)
        self.play(Create(point_on_graph), run_time=1)
        self.wait(2)
        # 2. Scene
        x1_val = float(table_data[1][1])  
        fx1_val = float(table_data[1][2])  
        x1_index = table.get_entries()[6]  
        x1_cell = table.get_entries()[7]   
        fx1_val_cell = table.get_entries()[8]  
        point_on_graph_1, x1_cross, x1_label, x1_vertical_line = create_point_elements(
            x1_val, fx1_val, 1
        )
        self.play(x1_index.animate.set_opacity(1), run_time=1)
        self.play(x1_cell.animate.set_opacity(1), run_time=1)
        self.play(Create(x1_cross), run_time=1)
        self.play(Write(x1_label), run_time=1)
        self.play(fx1_val_cell.animate.set_opacity(1), run_time=1)
        self.play(Create(x1_vertical_line), run_time=1)
        self.play(Create(point_on_graph_1), run_time=1)
        self.wait(2)
        # 3. Scene
        x2_val = float(table_data[2][1])  
        fx2_val = float(table_data[2][2])  
        x2_index = table.get_entries()[9]  
        x2_cell = table.get_entries()[10]  
        fx2_val_cell = table.get_entries()[11]  
        point_on_graph_2, x2_cross, x2_label, x2_vertical_line = create_point_elements(
            x2_val, fx2_val, 2
        )
        self.play(x2_index.animate.set_opacity(1), run_time=1)
        self.play(x2_cell.animate.set_opacity(1), run_time=1)
        self.play(Create(x2_cross), run_time=1)
        self.play(Write(x2_label), run_time=1)
        self.play(fx2_val_cell.animate.set_opacity(1), run_time=1)
        self.play(Create(x2_vertical_line), run_time=1)
        self.play(Create(point_on_graph_2), run_time=1)
        self.wait(2)
        # 4. Scene
        x3_val = float(table_data[3][1])  
        fx3_val = float(table_data[3][2])  
        x3_index = table.get_entries()[12]  
        x3_cell = table.get_entries()[13]   
        fx3_val_cell = table.get_entries()[14] 
        point_on_graph_3, x3_cross, x3_label, x3_vertical_line = create_point_elements(
            x3_val, fx3_val, 3
        )
        # Animate the elements
        self.play(x3_index.animate.set_opacity(1), run_time=1)
        self.play(x3_cell.animate.set_opacity(1), run_time=1)
        self.play(Create(x3_cross), run_time=1)
        self.play(Write(x3_label), run_time=1)
        self.play(fx3_val_cell.animate.set_opacity(1), run_time=1)
        self.play(Create(x3_vertical_line), run_time=1)
        self.play(Create(point_on_graph_3), run_time=1)
        self.wait(2)
        # 5. Scene: Remaining rows
        # Row 5
        x4_index = table.get_entries()[15]
        x4_cell = table.get_entries()[16]
        fx4_val_cell = table.get_entries()[17]
        self.play(x4_index.animate.set_opacity(1), run_time=1)
        self.play(x4_cell.animate.set_opacity(1), run_time=1)
        self.play(fx4_val_cell.animate.set_opacity(1), run_time=1)
        # Row 6
        x5_index = table.get_entries()[18]
        x5_cell = table.get_entries()[19]
        fx5_val_cell = table.get_entries()[20]
        self.play(x5_index.animate.set_opacity(1), run_time=1)
        self.play(x5_cell.animate.set_opacity(1), run_time=1)
        self.play(fx5_val_cell.animate.set_opacity(1), run_time=1)
        # Row 7
        x6_index = table.get_entries()[21]
        x6_cell = table.get_entries()[22]
        fx6_val_cell = table.get_entries()[23]
        self.play(x6_index.animate.set_opacity(1), run_time=1)
        self.play(x6_cell.animate.set_opacity(1), run_time=1)
        self.play(fx6_val_cell.animate.set_opacity(1), run_time=1)
        # Row 8
        x7_index = table.get_entries()[24]
        x7_cell = table.get_entries()[25]
        fx7_val_cell = table.get_entries()[26]
        self.play(x7_index.animate.set_opacity(1), run_time=1)
        self.play(x7_cell.animate.set_opacity(1), run_time=1)
        self.play(fx7_val_cell.animate.set_opacity(1), run_time=1)
        self.wait(2)
        # Create root marker and label
        x7_val = float(table_data[7][1])
        x_root = MathTex(
                r"\mathbf{\boldsymbol{X}}",
                color=RED
            ).scale(0.6).move_to(axes.c2p(x7_val, 0))
        x_root_label = MathTex(r"\text{root}", color=RED).scale(0.6).next_to(x_root, UP, buff=0.2)
        # Animate the root marker and label
        self.play(
            Create(x_root),
            Write(x_root_label),
            run_time=2
        )
        self.wait(2)

