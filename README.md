# AI_Avengers
# Autonomous Bot Navigation Simulation

## Table of Contents
- [Project Overview](#project-overview)
- [Key Features](#key-features)
- [Architecture and Components](#architecture-and-components)
- [Technology and Techniques](#technology-and-techniques)
- [How to Run the Project](#how-to-run-the-project)
- [Input Format](#input-format)
- [Contributors](#contributors)

## Project Overview

This project is an **autonomous bot navigation simulation** where multiple bots navigate a grid-based warehouse environment. The bots use **reinforcement learning** and **strategic pathfinding** to reach their designated goals while avoiding collisions with obstacles and other bots.

The project showcases how AI-driven bots can move autonomously in a confined space and efficiently reach their destinations without deadlocks or collisions. The system provides a fully customizable grid environment with support for multiple bots, obstacles, and rewards based on movement efficiency.

## Key Features

- **Reinforcement Learning**: Each bot learns from its environment to optimize its movements, reduce penalties, and avoid collisions.
- **Collision Avoidance**: The system detects and prevents bots from colliding with one another, applying penalties if necessary.
- **Deadlock Detection**: Bots are penalized for repetitive actions, helping them avoid deadlocks and loops.
- **Customizable Environment**: The grid, number of bots, and obstacles can be easily customized through input files.
- **Live Simulation**: A real-time simulation showcases the bots' movements, collision avoidance, and completion of goals.
- **Detailed Reporting**: After each simulation, a report is generated with details on total commands, penalties, collisions, and paths taken.

## Architecture and Components

This project consists of several key components:

1. **Autobot**: Each bot in the grid is an intelligent agent that uses reinforcement learning to decide its actions (move forward, turn left, right, wait, etc.). The bots are penalized for invalid or repetitive actions and rewarded for successfully navigating the grid.

2. **CentralController**: The simulation's core logic lies here. The Central Controller manages all the bots, tracks their movements, detects collisions, and applies penalties based on bot actions.

3. **WarehouseGrid**: Represents the grid environment in which bots navigate. It contains obstacles, tracks bot positions, and ensures bots don't move outside the grid or collide with obstacles.

4. **RewardStrategy**: Defines the reward system for the bots. It applies penalties for collisions, invalid moves, and repetitive actions, while rewarding bots for successfully reaching their destinations.

5. **Input Handling**: The system reads user inputs, such as grid dimensions, autobot positions, and obstacle locations, from a file (input.txt).

## Technology and Techniques

- **Python**: The entire simulation is written in Python, utilizing object-oriented programming principles.
- **Reinforcement Learning**: Bots learn through rewards and penalties, continuously improving their decision-making process.
- **Collision Detection**: A sophisticated collision detection system ensures that bots avoid one another.
- **Grid Environment**: The bots operate in a 2D grid environment, interacting with obstacles and other bots.


### Key Files:
- `main.py`: The entry point to run the simulation.
- `autobot/autobot.py`: Contains the logic for bot movement and decision-making.
- `controller/central_controller.py`: Manages the entire simulation, handles actions, detects collisions, and tracks progress.
- `environment/warehouse_grid.py`: Defines the environment (grid) where bots operate.
- `environment/reward_strategy.py`: Implements the reward and penalty system based on bot actions.
- `input.txt`: Defines the grid size, bots, and obstacles for the simulation.

## How to Run the Project

### Prerequisites:
- **Python 3.x** installed on your machine.
- Required Python libraries (install via `pip`):
  ```bash
  pip install matplotlib numpy

### Steps to Run:

- **1**: create virtual environment:
   ```python
  python -m venv myenv
  myenv\Scripts\activate
- **2**: Install all dependencies
- **3**: give input into input.txt
- **4**: if you want to GUI based on input.txt then run the project:
  ```python
  python main.py
- **5**: if you want to give input in GUI then run the project:
  ```python
  python bot_simulation_gui.py


### Input format for input.txt:
- 5 5              -> Grid size: 5 rows and 5 columns
- 2                -> Number of autobots

- 0 0 0 4          -> Autobot 1: Start at (0, 0), End at (0, 4)
- 4 0 4 4          -> Autobot 2: Start at (4, 0), End at (4, 4)

- 4                -> Number of obstacles

- 0 3              -> Obstacle at position (0, 3)
- 1 1              -> Obstacle at position (1, 1)
- 2 2              -> Obstacle at position (2, 2)
- 4 1              -> Obstacle at position (4, 1)


### Project structure
- |-- DoseHack24/
-   |-- README.md           
-   |-- requirements.txt    
-   |-- main.py             
-   |-- flow.txt      
-   |-- input.txt    
-   |-- bot_simulation_gui.py
-   |-- autobot/
       |-- autobot.py   
       |-- q_learning.py   
-   |-- controller/
       |-- central_controller.py   
       |-- test_q_learning.py      
-   |-- environment/
       |-- reward_strategy.txt        
       |-- warehouse_grid.py                   

