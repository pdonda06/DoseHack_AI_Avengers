import numpy as np
from autobot.qlearning import QLearningAgent

class Autobot:
    def __init__(self, id, start_position, end_position, grid_size, actions):
        self.id = id
        self.position = list(start_position)  # Start position converted to list
        self.end_position = end_position  # Destination can remain as a tuple
        self.grid_size = grid_size  # Size of the grid
        self.actions = actions  # List of possible actions
        self.agent = QLearningAgent(actions, grid_size)  # RL agent for learning optimal moves
        self.previous_distance_to_goal = self.calculate_distance_to_goal()

    def execute_action(self, action):
        """ Update position based on the selected action """
        if action == 'forward':
            self.position[1] = min(self.position[1] + 1, self.grid_size[1] - 1)  # Moving up (y-direction)
        elif action == 'reverse':
            self.position[1] = max(self.position[1] - 1, 0)  # Moving down (y-direction)
        elif action == 'left':
            self.position[0] = max(self.position[0] - 1, 0)  # Moving left (x-direction)
        elif action == 'right':
            self.position[0] = min(self.position[0] + 1, self.grid_size[0] - 1)  # Moving right (x-direction)
        elif action == 'wait':
            pass  # No movement for 'wait' action

    def choose_action(self, state):
        """ Choose an action based on the current state """
        return self.agent.choose_action(state)

    def get_state(self):
        """ Get current state (position) """
        return tuple(self.position)  # Return the position as a tuple

    def reached_destination(self):
        """ Check if the autobot has reached its destination """
        return tuple(self.position) == self.end_position

    def calculate_distance_to_goal(self):
        """ Calculate the Manhattan distance to the goal """
        x1, y1 = self.position
        x2, y2 = self.end_position
        return abs(x1 - x2) + abs(y1 - y2)
