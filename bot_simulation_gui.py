# import tkinter as tk
# from tkinter import messagebox
# from autobot.autobot import Autobot  # Assuming Autobot is in autobot.py
# from controller.central_controller import CentralController  # Assuming CentralController is in controller.py
# from environment.warehouse_grid import WarehouseGrid  # Assuming WarehouseGrid is in environment.py
# from environment.reward_strategy import RewardStrategy  # Assuming RewardStrategy is in environment.py


# class BotSimulationApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Autobot Simulation")

#         # Create input fields for grid dimensions and number of bots/obstacles
#         self.create_input_panel()

#     def create_input_panel(self):
#         """Create the input panel where users specify grid size, bots, and obstacles."""
#         frame = tk.Frame(self.root)
#         frame.grid(pady=10)

#         # Grid size inputs
#         tk.Label(frame, text="Grid Rows (M):").grid(row=0, column=0)
#         self.grid_rows_entry = tk.Entry(frame, width=5)
#         self.grid_rows_entry.grid(row=0, column=1)

#         tk.Label(frame, text="Grid Columns (N):").grid(row=0, column=2)
#         self.grid_columns_entry = tk.Entry(frame, width=5)
#         self.grid_columns_entry.grid(row=0, column=3)

#         # Number of bots and obstacles inputs
#         tk.Label(frame, text="Number of Bots:").grid(row=1, column=0)
#         self.num_bots_entry = tk.Entry(frame, width=5)
#         self.num_bots_entry.grid(row=1, column=1)

#         tk.Label(frame, text="Number of Obstacles:").grid(row=1, column=2)
#         self.num_obstacles_entry = tk.Entry(frame, width=5)
#         self.num_obstacles_entry.grid(row=1, column=3)

#         # Submit button
#         tk.Button(frame, text="Create Grid", command=self.create_grid).grid(row=2, column=1, pady=10)

#     def create_grid(self):
#         """Generate the grid based on user input and allow user to click cells to place bots/obstacles."""
#         try:
#             self.rows = int(self.grid_rows_entry.get())
#             self.columns = int(self.grid_columns_entry.get())
#             self.num_bots = int(self.num_bots_entry.get())
#             self.num_obstacles = int(self.num_obstacles_entry.get())
#         except ValueError:
#             messagebox.showerror("Input Error", "Please enter valid numbers.")
#             return

#         # Clear previous grid if exists
#         if hasattr(self, 'grid_frame'):
#             self.grid_frame.destroy()

#         self.grid_frame = tk.Frame(self.root)
#         self.grid_frame.grid()

#         self.grid_cells = {}  # Store references to grid buttons
#         self.bot_positions = []  # Track bot start/end positions
#         self.obstacle_positions = []  # Track obstacle positions
#         self.current_bot = 1  # Track which bot we're placing
#         self.placing_obstacles = False  # Check if we are placing obstacles

#         tk.Label(self.grid_frame, text="Click to place bot start and end positions").grid(row=self.rows + 1, column=0, columnspan=self.columns)

#         # Create grid of buttons
#         for r in range(self.rows):
#             for c in range(self.columns):
#                 btn = tk.Button(self.grid_frame, width=5, height=2, command=lambda r=r, c=c: self.place_bot_or_obstacle(r, c))
#                 btn.grid(row=r, column=c)
#                 self.grid_cells[(r, c)] = btn

#     def place_bot_or_obstacle(self, row, col):
#         """Handle click on grid cell to place bot start/end positions or obstacles."""
#         if len(self.bot_positions) < self.num_bots * 2:
#             # Place bot start/end position
#             if len(self.bot_positions) % 2 == 0:
#                 # Place start position
#                 self.grid_cells[(row, col)].config(text=f"B{self.current_bot} Start", bg="blue")
#             else:
#                 # Place end position
#                 self.grid_cells[(row, col)].config(text=f"B{self.current_bot} End", bg="green")
#                 self.current_bot += 1

#             self.bot_positions.append((row, col))

#             # When all bots are placed, allow placing obstacles
#             if len(self.bot_positions) == self.num_bots * 2:
#                 self.placing_obstacles = True
#                 tk.Label(self.grid_frame, text="Click to place obstacles").grid(row=self.rows + 2, column=0, columnspan=self.columns)

#         elif self.placing_obstacles and len(self.obstacle_positions) < self.num_obstacles:
#             # Place obstacles
#             self.grid_cells[(row, col)].config(text="X", bg="red")
#             self.obstacle_positions.append((row, col))

#             # Once all obstacles are placed, start the simulation
#             if len(self.obstacle_positions) == self.num_obstacles:
#                 self.run_simulation()

#     def run_simulation(self):
#         """Run the bot simulation and display the paths taken."""
#         tk.Label(self.grid_frame, text="Running simulation...").grid(row=self.rows + 3, column=0, columnspan=self.columns)

#         # Convert bot positions and obstacle positions for the simulation
#         bots = []
#         for i in range(0, len(self.bot_positions), 2):
#             start = self.bot_positions[i]
#             end = self.bot_positions[i + 1]
#             bots.append(Autobot(id=i // 2 + 1, start_position=start, end_position=end, grid_size=(self.rows, self.columns), actions=['forward', 'reverse', 'left', 'right', 'wait']))

#         # Initialize the WarehouseGrid and RewardStrategy
#         reward_strategy = RewardStrategy()
#         warehouse_grid = WarehouseGrid(grid_size=(self.rows, self.columns), obstacles=self.obstacle_positions, autobots=bots, reward_strategy=reward_strategy)

#         # Initialize the CentralController and start the simulation
#         controller = CentralController(warehouse_grid)
#         controller.simulate()

#         # Example: Display the simulation results
#         tk.Label(self.grid_frame, text="Simulation complete!").grid(row=self.rows + 4, column=0, columnspan=self.columns)

#         # Here you would visualize the bot movements on the grid, showing their paths, handling collisions, etc.


# if __name__ == "__main__":
#     root = tk.Tk()
#     app = BotSimulationApp(root)
#     root.mainloop()




import tkinter as tk
from tkinter import messagebox
from autobot.autobot import Autobot  # Assuming Autobot is in autobot.py
from controller.central_controller import CentralController  # Assuming CentralController is in controller.py
from environment.warehouse_grid import WarehouseGrid  # Assuming WarehouseGrid is in environment.py
from environment.reward_strategy import RewardStrategy  # Assuming RewardStrategy is in environment.py


class BotSimulationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Autobot Simulation")

        # Create input fields for grid dimensions and number of bots/obstacles
        self.create_input_panel()

    def create_input_panel(self):
        """Create the input panel where users specify grid size, bots, and obstacles."""
        frame = tk.Frame(self.root)
        frame.grid(pady=10)

        # Grid size inputs
        tk.Label(frame, text="Grid Rows (M):").grid(row=0, column=0)
        self.grid_rows_entry = tk.Entry(frame, width=5)
        self.grid_rows_entry.grid(row=0, column=1)

        tk.Label(frame, text="Grid Columns (N):").grid(row=0, column=2)
        self.grid_columns_entry = tk.Entry(frame, width=5)
        self.grid_columns_entry.grid(row=0, column=3)

        # Number of bots and obstacles inputs
        tk.Label(frame, text="Number of Bots:").grid(row=1, column=0)
        self.num_bots_entry = tk.Entry(frame, width=5)
        self.num_bots_entry.grid(row=1, column=1)

        tk.Label(frame, text="Number of Obstacles:").grid(row=1, column=2)
        self.num_obstacles_entry = tk.Entry(frame, width=5)
        self.num_obstacles_entry.grid(row=1, column=3)

        # Submit button
        tk.Button(frame, text="Create Grid", command=self.create_grid).grid(row=2, column=1, pady=10)

    def create_grid(self):
        """Generate the grid based on user input and allow user to click cells to place bots/obstacles."""
        try:
            self.rows = int(self.grid_rows_entry.get())
            self.columns = int(self.grid_columns_entry.get())
            self.num_bots = int(self.num_bots_entry.get())
            self.num_obstacles = int(self.num_obstacles_entry.get())
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers.")
            return

        if self.num_bots * 2 + self.num_obstacles > self.rows * self.columns:
            messagebox.showerror("Grid Error", "Not enough space for bots and obstacles in the grid.")
            return

        # Clear previous grid if exists
        if hasattr(self, 'grid_frame'):
            self.grid_frame.destroy()

        self.grid_frame = tk.Frame(self.root)
        self.grid_frame.grid()

        self.grid_cells = {}  # Store references to grid buttons
        self.bot_positions = []  # Track bot start/end positions
        self.obstacle_positions = []  # Track obstacle positions
        self.current_bot = 1  # Track which bot we're placing
        self.placing_obstacles = self.num_obstacles > 0  # Only place obstacles if the number is greater than 0

        tk.Label(self.grid_frame, text="Click to place bot start and end positions").grid(row=self.rows + 1, column=0, columnspan=self.columns)

        # Create grid of buttons
        for r in range(self.rows):
            for c in range(self.columns):
                btn = tk.Button(self.grid_frame, width=5, height=2, command=lambda r=r, c=c: self.place_bot_or_obstacle(r, c))
                btn.grid(row=r, column=c)
                self.grid_cells[(r, c)] = btn

    def place_bot_or_obstacle(self, row, col):
        """Handle click on grid cell to place bot start/end positions or obstacles."""
        if (row, col) in self.bot_positions or (row, col) in self.obstacle_positions:
            # Prevent placing bots/obstacles in an already occupied cell
            messagebox.showerror("Invalid Placement", "This cell is already occupied. Choose a different cell.")
            return

        if len(self.bot_positions) < self.num_bots * 2:
            # Place bot start/end position
            if len(self.bot_positions) % 2 == 0:
                # Place start position
                self.grid_cells[(row, col)].config(text=f"B{self.current_bot} Start", bg="blue")
            else:
                # Place end position
                self.grid_cells[(row, col)].config(text=f"B{self.current_bot} End", bg="green")
                self.current_bot += 1

            self.bot_positions.append((row, col))

            # When all bots are placed, allow placing obstacles or run simulation if no obstacles
            if len(self.bot_positions) == self.num_bots * 2:
                if self.num_obstacles > 0:
                    self.placing_obstacles = True
                    tk.Label(self.grid_frame, text="Click to place obstacles").grid(row=self.rows + 2, column=0, columnspan=self.columns)
                else:
                    # If no obstacles, run simulation immediately
                    self.run_simulation()

        elif self.placing_obstacles and len(self.obstacle_positions) < self.num_obstacles:
            # Place obstacles
            self.grid_cells[(row, col)].config(text="X", bg="red")
            self.obstacle_positions.append((row, col))

            # Once all obstacles are placed, start the simulation
            if len(self.obstacle_positions) == self.num_obstacles:
                self.run_simulation()

    def run_simulation(self):
        """Run the bot simulation and display the paths taken."""
        if len(self.bot_positions) < self.num_bots * 2:
            messagebox.showerror("Incomplete Setup", "Please place all bot start and end positions.")
            return

        tk.Label(self.grid_frame, text="Running simulation...").grid(row=self.rows + 3, column=0, columnspan=self.columns)

        # Convert bot positions and obstacle positions for the simulation
        bots = []
        for i in range(0, len(self.bot_positions), 2):
            start = self.bot_positions[i]
            end = self.bot_positions[i + 1]
            bots.append(Autobot(id=i // 2 + 1, start_position=start, end_position=end, grid_size=(self.rows, self.columns), actions=['forward', 'reverse', 'left', 'right', 'wait']))

        # Initialize the WarehouseGrid and RewardStrategy
        reward_strategy = RewardStrategy()
        warehouse_grid = WarehouseGrid(grid_size=(self.rows, self.columns), obstacles=self.obstacle_positions, autobots=bots, reward_strategy=reward_strategy)

        # Initialize the CentralController and start the simulation
        controller = CentralController(warehouse_grid)
        controller.simulate()

        # Example: Display the simulation results
        tk.Label(self.grid_frame, text="Simulation complete!").grid(row=self.rows + 4, column=0, columnspan=self.columns)

        # Here you would visualize the bot movements on the grid, showing their paths, handling collisions, etc.


if __name__ == "__main__":
    root = tk.Tk()
    app = BotSimulationApp(root)
    root.mainloop()
