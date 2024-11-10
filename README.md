Here's a detailed README file for your Tic-Tac-Toe game:

---

# Tic-Tac-Toe Game with ASCII Art and Turtle Graphics

This is a Python-based Tic-Tac-Toe game that can be played either in a **command-line interface (CLI)** using ASCII art or in a **graphical user interface (GUI)** using **Turtle Graphics**. The game provides two modes:
- **Player vs. Player:** Two players take turns.
- **Player vs. CPU:** The player competes against an AI, which uses the **MiniMax algorithm** for optimal decision-making.

## Table of Contents
1. [Features](#features)
2. [Requirements](#requirements)
3. [Installation and Setup](#installation-and-setup)
4. [How to Play](#how-to-play)
5. [Code Structure](#code-structure)
6. [Details of Key Functions](#details-of-key-functions)
7. [Usage](#usage)

---

## Features

- **Multiple Game Modes**: Play against another player or a CPU opponent.
- **CLI (ASCII Art)** and **GUI (Turtle Graphics)** displays for flexibility in user experience.
- **AI Opponent**: The CPU uses the MiniMax algorithm to make optimal moves.
- **Dynamic Game State Rendering**: The board updates automatically after each move in either CLI or GUI mode.

## Requirements

- **Python 3.x**
- **Turtle Graphics**: This is a built-in Python module for basic graphics.
- Optional libraries:
    - **GameSystem** and **MiniMax**: Custom modules for handling game logic and AI decision-making.
    - **turtleG**: Custom module for managing the Turtle graphics UI.

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/tic-tac-toe
   cd tic-tac-toe
   ```
2. Ensure that **Python 3.x** is installed on your system.
3. Install any dependencies if needed.

## How to Play

1. Run the game:
   ```bash
   python main.py
   ```
2. The game will display a welcome message in ASCII art.
3. Choose whether to play in **CLI (ASCII)** or **GUI (Turtle Graphics)** mode.
4. Select your game mode:
   - In **CLI mode**: Choose to play against the CPU or another player.
   - In **GUI mode**: Simply follow the prompts to play the game.

## Code Structure

### Key Modules and Files
- `main.py`: This is the main file where the game is initialized and run.
- `GameSystem`: Manages the overall game state, including move validation and win checking.
- `MiniMax`: Contains the logic for the AI's MiniMax algorithm, allowing the CPU to make optimal moves.
- `turtleG`: Handles the Turtle graphics display, including drawing the game board and player moves.

### Function Overview

| Function                | Description                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------------------|
| `print_ascii_art`       | Renders the tic-tac-toe board as ASCII art, showing current game state.                           |
| `display_type`          | Chooses between CLI (ASCII) or GUI (Turtle Graphics) based on user selection.                     |
| `display_turtle_graphics`| Updates the game board in Turtle Graphics to show current moves by players or CPU.               |
| `play_with_cpu`         | Manages game loop for player vs. CPU mode, utilizing the MiniMax algorithm for CPU moves.         |
| `play_with_player`      | Manages game loop for player vs. player mode.                                                     |
| `play_type`             | Prompts the user to choose the display type and game mode (CPU or Player).                        |
| `main`                  | Initializes and starts the game, displaying the welcome message and managing user input.          |

## Details of Key Functions

### 1. `print_ascii_art()`
This function creates a visual representation of the game board in ASCII art format, iterating over each row to show the board’s state dynamically as moves are made.

### 2. `display_type(play_view)`
This function determines whether to display the game using ASCII art or Turtle Graphics based on the `play_view` flag. ASCII art is printed in the console, while Turtle Graphics opens a graphical window.

### 3. `display_turtle_graphics()`
Manages the game board display using Turtle Graphics. For each move, it draws an `X` or `O` symbol on the board based on the player’s input or CPU’s choice.

### 4. `play_with_cpu(play_view)`
Runs the game loop for a player vs. CPU match. The function alternates turns, checks for wins, and utilizes the MiniMax algorithm for CPU moves.

### 5. `play_with_player(play_view)`
Runs the game loop for a player vs. player match. Players take turns until a win condition is met or the board is full.

### 6. `play_type(play_view)`
Handles initial setup and prompts the user to select between CLI and GUI modes and whether to play against the CPU or another player.

### 7. `main()`
The main entry point for the game. This function displays the welcome message, prompts the user for settings, and starts the game loop.

## Usage

Run the game, choose between playing in CLI or GUI mode, and enjoy a game of Tic-Tac-Toe against another player or a CPU opponent with AI capabilities!

**Example Execution:**
```bash
python3 main.py
```

**Sample Console Output:**
```plaintext
               .__                                  __             __  .__           __                    __                  ._.
__  _  __ ____ |  |   ____  ____   _____   ____   _/  |_  ____   _/  |_|__| ____   _/  |______    ____   _/  |_  ____   ____   | |
\ \/ \/ // __ \|  | _/ ___\/  _ \ /     \_/ __ \  \   __\/  _ \  \   __\  |/ ___\  \   __\__  \ _/ ___\  \   __\/  _ \_/ __ \  | |
 \     /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/   |  | (  <_> )  |  | |  \  \___   |  |  / __ \\  \___   |  | (  <_> )  ___/   \|
  \/\_/  \___  >____/\___  >____/|__|_|  /\___  >  |__|  \____/   |__| |__|\___  >  |__| (____  /\___  >  |__|  \____/ \___  >  __
             \/          \/            \/     \/                               \/             \/     \/                    \/   \/

Do you want to play with the CLI or GUI? (CLI/GUI): cli
ASCII Art
Do you want to play with CPU or Player? (CPU/Player): player
...
Game Over
Thanks for playing
Bye!
```

---

