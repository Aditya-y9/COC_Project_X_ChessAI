# ChessAI


### README.md file is at its most basic version and will be updated soon as we progress with the project.
### Thank you for your patience.

## Index
<ul>
    <li><a href="#about-the-project">About the Project</a></li>
    <li><a href="#tech-stack">Tech Stack</a></li>
    <li><a href="#file-structure">File Structure</a></li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#features">Features</a></li>
    <li><a href="#usage">Usage</a></li>

## About the Project

### Aim: 
#### To create a chess AI that can play against a human player.

### Description:
#### The project is a chess AI that can play against a human player. The AI uses the NegMax algorithm with alpha-beta pruning to determine the best move at each gamestate.
<text>
    The project is written in Python and uses the pygame library for the GUI. The AI uses the NegMax algorithm with alpha-beta pruning to determine the best move at each gamestate. The AI is also able to play against itself.
    The AI understands each game state by assigining an evaluation score to each possible gamestate.
    The AI considers the following factors when assigning an evaluation score to a gamestate:
    <ul>
        <li>Material Advantage</li>
        <li>Positional Advantage</li>
        <li>King Safety</li>
        <li>Castling</li>
        <li>King Castling</li>
        <li>Checkmate</li>
        <li>Stalemate</li>
    </ul>
    Based on these factors, the AI assigns an evaluation score to each gamestate. 
    Then the AI uses the NegMax algorithm with alpha-beta pruning to determine the best move at each gamestate.
</text>

## Tech Stack
This project is built using the following technologies:
<ul>
    <li>Python
    <p>
    Python is a programming language that lets you work quickly and integrate systems more effectively.
    It is popular because of its clear syntax and readability.
    </p>
    </li>
    <li>Pygame
    <p>
    Pygame is a set of Python modules designed for writing video games. It includes computer graphics and sound libraries that are designed to be used with the Python programming language. Pygame provides an easy-to-use interface for creating games and multimedia applications. It is cross-platform, which means that it can be used on different operating systems such as Windows, macOS, and Linux. Pygame is built on top of the SDL library, which provides low-level access to audio, keyboard, mouse, joystick, and graphics hardware. With Pygame, you can create 2D games, 3D games, and multimedia applications.Pygame is a set of Python modules designed for writing video games. It includes computer graphics and sound libraries that are designed to be used with the Python programming language. Pygame provides an easy-to-use interface for creating games and multimedia applications. It is cross-platform, which means that it can be used on different operating systems such as Windows, macOS, and Linux. Pygame is built on top of the SDL library, which provides low-level access to audio, keyboard, mouse, joystick, and graphics hardware. With Pygame, you can create 2D games, 3D games, and multimedia applications.
    </p>
    </li>
    <li>Numpy
    <p>
    NumPy is a Python library used for working with arrays. It also has functions for working in domain of linear algebra, fourier transform, and matrices. NumPy was created in 2005 by Travis Oliphant. It is an open source project and you can use it freely. NumPy stands for Numerical Python.
    </p>
    </li>
</ul>

## File Structure
```
.

├── ChessAI
│   ├── AI.py
│   ├── engine.py
│   ├── main.py

.
``` 
## Getting Started
### Dependencies
<ul>
    <li>Python 3</li>
    <li>Pygame</li>
    <li>Numpy</li>
</ul>


### Installation
<ol>
    <li>Clone the repository
    </li>
    <li>
    Select whether you want to play versus computer, against another player locally, or watch the game of two computers
    From the Appropriate flag in the main.py file
    <code>
    '''
    playerone = True
    playertwo = False
    Indicates that the player is playing against the computer
    True indicates that the player is a human player
    False indicates that the player is a computer player
    '''
    </code>
    </li>
            <li>Install pygame
                    <ul>
                        <li>On the Terminal, run:</li>
                    <code>pip install pygame</code>
                    <li>Pygame should get installed</ul>
                <li>Run main.py</li>
                <li><code>python main.py</code>
                <li>The Home Screen of the Game should appear on your screen</li>
            </ol>
        </ul>
</ol>

### Features
<ul>
    <li>Play against the computer</li>
    <li>Play against another player locally</li>
    <li>Watch the game of two computers</li>
    <li>Live Valid Move Checking</li>
    <li>Castling</li>
    <li>En Passant</li>
    <li>Promotion with its own menu</li>
    <li>Checkmate</li>
    <li>Stalemate</li>
    <li>Undo Moves</li>
    <li>Reset Game</li>
</ul>

### Usage
<ul>
    <li>Run main.py</li>
    <li>The Home Screen of the Game should appear on your screen</li>
    <li>Follow the message on the screen
    <ul><code>
    Press any key to start the game
    </code>
    </ul></li>
    <li>The Game Screen should appear on your screen</li>
    <li>Click a Chess piece to highlight it Valid Landing Squares</li>
    <li>Click a Valid Landing Square to move the Chess piece to that square</li>
    <li>Use<code>Ctrl + Z</code> Button to undo a move</li>
    <li>Use<code>Ctrl + R</code> Button to reset the game</li>
    <li>If Pawn Promotion occurs for the pawn of the human player, follow the instructions on the on-screen menu to do pawn promotion to your chosen piece</li>
    <li>Play the game until Checkmate or Stalemate occurs</li>

</ul>











