# import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib.animation import FuncAnimation

# class CentralController:
#     def __init__(self, grid, max_steps=1000):
#         self.grid = grid
#         self.total_time = 0  # Only count valid time steps
#         self.total_commands = {autobot.id: 0 for autobot in self.grid.autobots}  # Track total commands per autobot
#         self.autobot_actions_history = {autobot.id: [] for autobot in self.grid.autobots}  # Initialize actions history
#         self.last_position = {autobot.id: None for autobot in self.grid.autobots}  # Store the last position of autobots
#         self.collision_count = 0  # Track collision count
#         self.steps = []  # Store the state of the grid at each time step for animation
#         self.max_steps = max_steps  # Maximum number of steps allowed before detecting an impossible scenario

#     def simulate(self):
#         step = 0
#         while not all(autobot.reached_destination() for autobot in self.grid.autobots):
#             step += 1
#             if step > self.max_steps:
#                 print(f"Impossible scenario detected after {self.max_steps} commands. Deadlock or blocked paths.")
#                 break

#             valid_step = False  # Track whether a valid move happened in this step
#             autobot_actions = {}
#             occupied_positions = set()

#             print(f"\nTime step: {step}")

#             # Gather actions for each autobot
#             for autobot in self.grid.autobots:
#                 if not autobot.reached_destination():
#                     state = autobot.get_state()
#                     action = autobot.choose_action(state)
#                     action = str(action)  # Convert to string
#                     autobot_actions[autobot] = action
#                     print(f"Autobot {autobot.id} chooses action {action} from state {state}")

#             # Resolve movements and handle collisions
#             for autobot, action in autobot_actions.items():
#                 next_position = self.grid.calculate_next_position(autobot, action)

#                 # Check for repeated back-and-forth movements
#                 if next_position == self.last_position[autobot.id]:
#                     print(f"Autobot {autobot.id} is repeating moves.")
#                     reward = -15  # Penalize for repetitive actions
#                     finished = False
#                 elif self.grid.is_valid_move(next_position):
#                     next_state, reward, finished = self.grid.step(autobot, action)
#                     self.last_position[autobot.id] = autobot.position  # Update the last position
#                     occupied_positions.add(tuple(next_state))
#                     self.total_commands[autobot.id] += 1  # Count valid move
#                     self.autobot_actions_history[autobot.id].append(action)
#                     valid_step = True  # Mark the step as valid since there was a valid move
#                 else:
#                     reward, finished = -5, False  # Invalid move penalty
#                     print(f"Invalid move by Autobot {autobot.id}: {action} - Out of bounds or obstacle.")
#                     next_position = autobot.position  # Autobots stay in position after an invalid move

#                 print(f"Autobot {autobot.id} moves to {next_position} with reward: {reward}")
#                 autobot.agent.learn(autobot.get_state(), action, reward, next_position)

#                 if finished:
#                     print(f"Autobot {autobot.id} has reached the destination.")

#             # Only increment the total time step if a valid move happened
#             if valid_step:
#                 self.total_time += 1
#                 self.steps.append((self.grid.grid.copy(), [autobot.position for autobot in self.grid.autobots]))

#         # Once all autobots have reached their destination, print the summary
#         self.generate_final_report()

#     def generate_final_report(self):
#         # Calculate total movements, average movements, and maximum movements
#         total_commands = sum(self.total_commands.values())
#         num_bots = len(self.grid.autobots)
#         avg_commands = total_commands / num_bots
#         max_commands = max(self.total_commands.values())

#         print(f"\n🚦 Test Case Summary 🚦")
#         print(f"Total Time Taken (Valid Steps): {self.total_time} units")
#         print(f"Total Collisions: {self.collision_count}")

#         for autobot in self.grid.autobots:
#             print(f"Total Commands for Autobot {autobot.id}: {self.total_commands[autobot.id]} commands")
#             print(f"Actions History for Autobot {autobot.id}: {self.autobot_actions_history[autobot.id]}")

#         print(f"\n📊 Final Matrix Report 📊")
#         print(f"Average Commands: {avg_commands:.2f}")
#         print(f"Maximum Commands (when the test case finishes): {max_commands}")

#         # Visualize the steps
#         visualize_grid_animation(self.grid.grid, self.grid.autobots, self.steps)


# def visualize_grid_animation(grid, autobots, steps):
#     fig, ax = plt.subplots(figsize=(8, 8))

#     def update(frame):
#         grid, autobot_positions = steps[frame]
#         ax.clear()

#         # Create visual grid representation
#         visual_grid = np.zeros((len(grid), len(grid[0])))

#         # Mark obstacles, but handle case with zero obstacles
#         for i in range(len(grid)):
#             for j in range(len(grid[i])):
#                 if grid[i][j] == 'X':  # Obstacles
#                     visual_grid[i][j] = 0.5  # Gray for obstacles

#         # Mark autobots, ensuring no two autobots share the same position
#         autobot_set = set()
#         for autobot, position in zip(autobots, autobot_positions):
#             x, y = position
#             if (x, y) not in autobot_set:  # Ensure no two autobots share the same cell
#                 visual_grid[x][y] = 1  # Mark autobot
#                 autobot_set.add((x, y))

#         ax.imshow(visual_grid, cmap='Blues', interpolation='nearest')

#         # Annotate autobots
#         for autobot, position in zip(autobots, autobot_positions):
#             ax.text(position[1], position[0], f'A{autobot.id}', color='red', ha='center', va='center', fontsize=12)

#         ax.set_title(f"Time Step: {frame + 1}")

#     ani = FuncAnimation(fig, update, frames=len(steps), repeat=False, interval=500)
#     plt.show()


import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

class CentralController:
    def __init__(self, grid, max_steps=1000):
        self.grid = grid
        self.total_time = 0  # Only count valid time steps
        self.total_commands = {autobot.id: 0 for autobot in self.grid.autobots}  # Track total commands per autobot
        self.autobot_actions_history = {autobot.id: [] for autobot in self.grid.autobots}  # Initialize actions history
        self.last_position = {autobot.id: None for autobot in self.grid.autobots}  # Store the last position of autobots
        self.collision_count = 0  # Track total collision count
        self.steps = []  # Store the state of the grid at each time step for animation
        self.max_steps = max_steps  # Maximum number of steps allowed before detecting an impossible scenario
        self.impossible_scenario = False  # Track if an impossible scenario has been detected

    def simulate(self):
        step = 0
        while not all(autobot.reached_destination() for autobot in self.grid.autobots):
            step += 1
            if step > self.max_steps:
                self.impossible_scenario = True
                print(f"Impossible scenario detected after {self.max_steps} commands. Deadlock or blocked paths.")
                break

            valid_step = False  # Track whether a valid move happened in this step
            autobot_actions = {}
            occupied_positions = {}  # Track occupied positions to detect collisions

            print(f"\nTime step: {step}")

            # Gather actions for each autobot
            for autobot in self.grid.autobots:
                if not autobot.reached_destination():
                    state = autobot.get_state()
                    action = autobot.choose_action(state)
                    action = str(action)  # Convert to string
                    autobot_actions[autobot] = action
                    print(f"Autobot {autobot.id} chooses action {action} from state {state}")

            # Resolve movements and handle collisions
            for autobot, action in autobot_actions.items():
                next_position = self.grid.calculate_next_position(autobot, action)

                # Check for repeated back-and-forth movements
                if next_position == self.last_position[autobot.id]:
                    print(f"Autobot {autobot.id} is repeating moves.")
                    reward = -15  # Penalize for repetitive actions
                    finished = False
                elif self.grid.is_valid_move(next_position):
                    # Detect if another autobot is already moving to the same position
                    if tuple(next_position) in occupied_positions:
                        print(f"Collision detected! Autobot {autobot.id} collided at position {next_position}")
                        self.collision_count += 1  # Increment collision count
                        reward, finished = -10, False  # Penalize for collision
                    else:
                        occupied_positions[tuple(next_position)] = autobot.id  # Mark position as occupied

                    next_state, reward, finished = self.grid.step(autobot, action)
                    self.last_position[autobot.id] = autobot.position  # Update the last position
                    self.total_commands[autobot.id] += 1  # Count valid move
                    self.autobot_actions_history[autobot.id].append(action)
                    valid_step = True  # Mark the step as valid since there was a valid move
                else:
                    reward, finished = -5, False  # Invalid move penalty
                    print(f"Invalid move by Autobot {autobot.id}: {action} - Out of bounds or obstacle.")
                    next_position = autobot.position  # Autobots stay in position after an invalid move

                print(f"Autobot {autobot.id} moves to {next_position} with reward: {reward}")
                autobot.agent.learn(autobot.get_state(), action, reward, next_position)

                if finished:
                    print(f"Autobot {autobot.id} has reached the destination.")

            # Only increment the total time step if a valid move happened
            if valid_step:
                self.total_time += 1
                self.steps.append((self.grid.grid.copy(), [autobot.position for autobot in self.grid.autobots]))

        # Once all autobots have reached their destination or scenario is impossible, print the summary
        self.generate_final_report()

    def generate_final_report(self):
        # Calculate total movements, average movements, and maximum movements
        total_commands = sum(self.total_commands.values())
        num_bots = len(self.grid.autobots)
        avg_commands = total_commands / num_bots
        max_commands = max(self.total_commands.values())

        print(f"\n🚦 Test Case Summary 🚦")
        print(f"Total Time Taken (Valid Steps): {self.total_time} units")
        print(f"Total Collisions: {self.collision_count}")

        for autobot in self.grid.autobots:
            print(f"Total Commands for Autobot {autobot.id}: {self.total_commands[autobot.id]} commands")
            print(f"Actions History for Autobot {autobot.id}: {self.autobot_actions_history[autobot.id]}")

        if self.impossible_scenario:
            print(f"\n❌ Impossible Scenario Detected ❌")
            print(f"The simulation was terminated after {self.max_steps} commands due to either a deadlock or blocked paths.")
            print(f"Some bots may be stuck in loops, repeating moves, or unable to reach their destination.")

        print(f"\n📊 Final Matrix Report 📊")
        print(f"Average Commands: {avg_commands:.2f}")
        print(f"Maximum Commands (when the test case finishes): {max_commands}")

        # Visualize the steps if possible
        if not self.impossible_scenario:
            visualize_grid_animation(self.grid.grid, self.grid.autobots, self.steps)
        else:
            print("\nSkipping visualization due to an impossible scenario.")

# Visualization function (same as before)
def visualize_grid_animation(grid, autobots, steps):
    fig, ax = plt.subplots(figsize=(8, 8))

    def update(frame):
        grid, autobot_positions = steps[frame]
        ax.clear()

        # Create visual grid representation
        visual_grid = np.zeros((len(grid), len(grid[0])))

        # Mark obstacles
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 'X':  # Obstacles
                    visual_grid[i][j] = 0.5  # Gray for obstacles

        # Mark autobots, ensuring no two autobots share the same position
        autobot_set = set()
        for autobot, position in zip(autobots, autobot_positions):
            x, y = position
            if (x, y) not in autobot_set:  # Ensure no two autobots share the same cell
                visual_grid[x][y] = 1  # Mark autobot
                autobot_set.add((x, y))

        ax.imshow(visual_grid, cmap='Blues', interpolation='nearest')

        # Annotate autobots
        for autobot, position in zip(autobots, autobot_positions):
            ax.text(position[1], position[0], f'A{autobot.id}', color='red', ha='center', va='center', fontsize=12)

        ax.set_title(f"Time Step: {frame + 1}")

    ani = FuncAnimation(fig, update, frames=len(steps), repeat=False, interval=500)
    plt.show()
