class RewardStrategy:
    def __init__(self):
        pass

    def calculate_reward(self, autobot, next_position, grid, collision=False):
        """Calculates the reward for a given autobot action based on the next position and the grid state."""
        
        # Reward for reaching the destination
        if next_position == autobot.end_position:
            return 100, True  # High reward for reaching the destination

        # Penalty for collisions
        if collision:
            return -20, False  # Heavy penalty for colliding with another bot

        # Penalty for moving into obstacles
        if grid[next_position[0]][next_position[1]] == 'X':
            return -10, False  # Penalty for moving into an obstacle

        # Penalty for moving out of bounds
        if not (0 <= next_position[0] < len(grid) and 0 <= next_position[1] < len(grid[0])):
            return -5, False  # Penalty for moving out of bounds

        # Reward/Penalty for moving closer/further from the goal
        current_dist = autobot.calculate_distance_to_goal()
        new_dist = abs(next_position[0] - autobot.end_position[0]) + abs(next_position[1] - autobot.end_position[1])

        if new_dist < current_dist:
            return 1, False  # Small positive reward for getting closer
        else:
            return -1, False  # Penalty for moving away from the destination
