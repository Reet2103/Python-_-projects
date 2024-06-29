**Tic Tac Toe Game**
This repository contains a Tic Tac Toe game implemented in Python, designed to be played in both single-player (against a computer or AI) and multiplayer modes. The game logic is encapsulated within the fun() function, which manages all game functionalities using a list named "Board" to represent the game board.

Features:-
Single-player mode: Play against a computer or AI.
Multiplayer mode: Play against another human player.
Dynamic game board: The game board state is dynamically updated and displayed during gameplay.

Implementation Details:-
The game includes several key components and functions:

Analysis of Board (analyze_board()): This function analyzes the current state of the game board to determine if a player has won or if the game is a draw.

Board Representation (const_board()): This function displays the current state of the board, showing the positions of X's and O's as the game progresses.

User 1 Turn (user1_turn()): Manages the turn-taking for the first human player in multiplayer mode.

User 2 Turn (user2_turn()): Controls the turn-taking for the second human player in multiplayer mode.

Computer Turn (comp_turn()): Implements the turn-taking logic for the computer player in single-player mode. This function uses the Minimax algorithm, incorporating both Breadth-First Search (BFS) and Depth-First Search (DFS) approaches, to make strategic moves and provide a challenging gameplay experience.

How to Play:-
Single-player Mode
In single-player mode, you will play against the computer. The computer uses advanced AI techniques to play competitively.

Multiplayer Mode:-
In multiplayer mode, two human players take turns to place their markers (X or O) on the board.

Contact
If you have any questions or suggestions,feel free to contactat - reetbhardwaj2103@gmail.com
