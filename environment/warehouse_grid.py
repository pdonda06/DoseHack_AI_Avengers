class WarehouseGrid:
    def __init__(self, grid_size, obstacles, autobots, reward_strategy):
        self.grid_size = grid_size
        self.obstacles = obstacles
        self.autobots = autobots
        self.reward_strategy = reward_strategy
        self.grid = [['.' for _ in range(grid_size[1])] for _ in range(grid_size[0])]

        # Place obstacles on the grid
        for obstacle in obstacles:
            self.grid[obstacle[0]][obstacle[1]] = 'X'  # Mark obstacle positions with 'X'

    def step(self, autobot, action):
        """Execute the action for the autobot and return the next state, reward, and whether the destination was reached."""
        
        next_position = self.calculate_next_position(autobot, action)

        if not self.is_valid_move(next_position):
            return autobot.position, -5, False  # Invalid move: Out of bounds or obstacle

        # Call RewardStrategy to calculate reward based on next position and grid state
        reward, finished = self.reward_strategy.calculate_reward(autobot, next_position, self.grid)
        autobot.position = next_position  # Update autobot position

        return next_position, reward, finished

    def calculate_next_position(self, autobot, action):
        """Calculate the next position based on the current position and action."""
        r, c = autobot.position
        if action == 'forward':  # Move up (north), since facing north
            return r - 1, c
        elif action == 'reverse':  # Move down (south)
            return r + 1, c
        elif action == 'left':  # Move left (west)
            return r, c - 1
        elif action == 'right':  # Move right (east)
            return r, c + 1
        elif action == 'wait':
            return r, c  # Wait action doesn't move the bot
        else:
            return autobot.position  # Invalid action returns current position

    def is_valid_move(self, next_position):
        """Check if the move is valid (within bounds and not into an obstacle)."""
        r, c = next_position
        if not (0 <= r < self.grid_size[0] and 0 <= c < self.grid_size[1]):
            return False  # Out of bounds
        if self.grid[r][c] == 'X':  # Check for obstacle
            return False
        return True
