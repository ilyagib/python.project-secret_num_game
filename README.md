# Python Pygame Collection: Tic-Tac-Toe & Bagels
Python Pygame Collection: Classic Games 🎮
This repository features two interactive desktop games developed in Python. The project showcases my transition from console-based logic to Graphical User Interfaces (GUI) using the Pygame library, which I mastered through independent study.

🕹️ Included Games
1. Tic-Tac-Toe (TIC-TAC-TOE.py)
A polished version of the classic game featuring a human-vs-computer mode.

Key Technical Features:

2D List Board Representation: The game board is managed using a nested list structure (board = [["", "", ""], ...]) to track player moves.

Smart Computer Opponent: Implemented priority-based logic: the computer first checks for a winning move, then attempts to block the player, and finally picks a random empty cell.

Dynamic UI: Responsive grid rendering and a dedicated "Game Over" overlay.

2. Bagels (BAGELS_GAME.py)
A logic-based deduction game where you must guess a secret 3-digit number based on clues.

Key Technical Features:

List Manipulation: Extensive use of lists for generating unique secret numbers and tracking guess history.

Deductive Clue Logic: An algorithm that iterates through lists to return "Fermi" (correct digit/position), "Pico" (correct digit/wrong position), or "Bagels" (none correct).

Game State Management: Tracks variables like guesses_left and game_over to control the flow of the application.

🛠️ Skills & Technologies
Language: Python 3.x.

Library: Pygame (Handling the Game Loop, Surface Rendering, and Event Listeners).

Data Structures: * 2D Lists: For grid-based game state management.

Dynamic Lists: For tracking history and randomized secret codes.

Algorithms: Logic for win-conditions and pattern matching for clues.

🚀 Getting Started
Prerequisites
Make sure you have Python and Pygame installed:

Bash:

pip install pygame
Running the Games
To play Tic-Tac-Toe:

Bash:

python TIC-TAC-TOE.py
To play Bagels:

Bash:

python BAGELS_GAME.py
📖 Independent Study Focus
As part of my academic journey, I chose to go beyond the standard curriculum and explore Pygame. This involved:

Understanding the Game Loop architecture (Input -> Logic -> Render).

Learning Coordinate Geometry for positioning elements on a 2D screen.

Managing Events to handle real-time keyboard and mouse input.
