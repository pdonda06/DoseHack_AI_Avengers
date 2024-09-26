from autobot.autobot import Autobot
from environment.warehouse_grid import WarehouseGrid
from controller.central_controller import CentralController
from environment.reward_strategy import RewardStrategy
def get_user_input_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Read grid size
    grid_size = list(map(int, lines[0].strip().split()))
    M, N = grid_size  # M = rows, N = columns

    # Read number of autobots
    num_autobots = int(lines[1].strip())

    autobots = []
    line_index = 2
    for i in range(num_autobots):
        # Read start and end positions for each autobot
        start_end = list(map(int, lines[line_index].strip().split()))
        start_row, start_col, end_row, end_col = start_end
        autobots.append(Autobot(
            id=i + 1,
            start_position=(start_row, start_col),
            end_position=(end_row, end_col),
            grid_size=(M, N),
            actions=['forward', 'reverse', 'left', 'right', 'wait']
        ))
        line_index += 1

    # Read number of obstacles
    num_obstacles = int(lines[line_index].strip())
    line_index += 1

    obstacles = []
    for i in range(num_obstacles):
        # Read the obstacle positions
        obstacle = list(map(int, lines[line_index].strip().split()))
        obstacles.append(tuple(obstacle))
        line_index += 1

    # Create the grid (M x N)
    grid = [['.' for _ in range(N)] for _ in range(M)]
    
    # Mark obstacles in the grid
    for obstacle in obstacles:
        grid[obstacle[0]][obstacle[1]] = 'X'

    return grid, autobots, obstacles


def main():
    # Replace user input with file input for testing
    grid, autobots, obstacles = get_user_input_from_file('input.txt')

    # Initialize WarehouseGrid and RewardStrategy
    reward_strategy = RewardStrategy()

    # Initialize warehouse environment and controller with obstacles
    warehouse_grid = WarehouseGrid(grid_size=(len(grid), len(grid[0])), obstacles=obstacles, autobots=autobots, reward_strategy=reward_strategy)
    controller = CentralController(warehouse_grid)

    # Run the simulation
    controller.simulate()


if __name__ == '__main__':
    main()
