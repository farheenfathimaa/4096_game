# 4096 Game

## Introduction

4096 is a single-player sliding puzzle game where the goal is to slide numbered tiles on a grid to combine them and create a tile with the number 4096. You can continue playing the game after reaching the initial goal to create tiles with even larger numbers.

## Features

- Play the classic 4096 game in the terminal.
- Use the arrow keys to move tiles in different directions: left, right, up, and down.
- Merge tiles with the same number to create larger tiles.
- The game board fills up with new tiles to challenge you.
- Enjoy a text-based, console-style user interface.

## How to Play

1. Clone or download the repository to your local machine.
2. Open a terminal and navigate to the game directory.
3. Run the game with the following command:

   ```bash
   python 4096_game.py
   ```

4. Use the arrow keys (left, right, up, down) to move tiles.
5. Merge tiles with the same number to reach the goal of 4096.
6. Continue playing to achieve higher tile numbers.
7. Press 'q' to exit the game when you're done.

## Game Modes

You can customize the game by changing the `size` variable in the code:

- `size = 4`: Simple 4x4 board (default).
- Change the `size` value to create different game modes:
  - `size = 5`: Standard 5x5 board.
  - `size = 6`: Advanced 6x6 board.

## Dependencies

- Python 3.x
- curses library (for terminal-based UI)

## Credits

This game was created by Farheen Fathima as a simple implementation of the 4096 puzzle game.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
