<h1 style="text-align:center"> ChessAI </h1>


###### README.md file is at its most basic version and will be updated soon as we progress with the project.
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
#### To create a highly intelligent AI opponent for players to play using the NegMax algorithm for evaluation of different possible moves and then choosing the best on the basis of evaluation score.

### Description:
#### The project is a chess AI that can play against a human player. The AI uses the NegMax algorithm with alpha-beta pruning to determine the best move at each gamestate.
<text>
    The project is written in Python and uses the pygame library for the GUI. The AI uses the NegMax algorithm with alpha-beta pruning to determine the best move at each gamestate. The AI is also able to play against itself.
    The AI understands each game state by assigining an evaluation score to each possible gamestate.
    The AI considers the following factors when assigning an evaluation score to a gamestate:
    <ul>
        <li>Material</li>
        <li>Positional Advantage
        <ul>
            <li>Control of the center</li>
            <li>Control of the center files</li>
            <li>Control of the center ranks</li>
            <li>Control of the center diagonals</li>
            <li>Control of the center squares</li>
            <li>Control of the center squares</li>
        </ul>
        <li>King Safety
            <li>Castling</li>
            <li>King's
            <ul>
                <li>Position</li>
                <li>Number of pieces attacking it</li>
                <li>Number of pieces defending it</li>
            </ul>
            <li>Number of pieces defending the King</li>
            <li>
            Double Pawns
            </li>
            <li>
            Queen Mobility
            </li>
            <li>
            King Mobility
            </li>
            <li>
            Freedom of Movement
            </li>
            <li>
            Knight Support
            </li>
        </li> 

    Based on these factors, the AI assigns an evaluation score to each gamestate. 
    Then the AI uses the NegMax algorithm with alpha-beta pruning to determine the best move at each gamestate.
</text>

## Tech Stack
This project is built using the following technologies:
<ul>
    <li>Python</li>
    <li>
    Pygame
    <ul>
    <ul>
        <li>Pygame is a Python library that is commonly used for developing 2D games. It provides a set of modules that allow developers to create games and multimedia applications. Pygame is built on top of the Simple DirectMedia Layer (SDL) library, which provides low-level access to audio, keyboard, mouse, joystick, and graphics hardware.</li>
        <li>Pygame is a popular choice for game development because it is easy to learn and use, and it provides a lot of functionality out of the box. It includes modules for handling graphics, sound, input, and networking, among other things.</li>
        <li>In the context of the provided code excerpt, Pygame is being used to build a chess game.Pygame is a Python library that is commonly used for developing 2D games. It provides a set of modules that allow developers to create games and multimedia applications. Pygame is built on top of the Simple DirectMedia Layer (SDL) library, which provides low-level access to audio, keyboard, mouse, joystick, and graphics hardware.</li>
        <li>Pygame is a popular choice for game development because it is easy to learn and use, and it provides a lot of functionality out of the box. It includes modules for handling graphics, sound, input, and networking, among other things.</li>
        <li>Pygame is being used to build a chess game.</li>
    </ul>
    </ul>
<ul>
    </li>
    <li>Numpy
    <ul>
    <li>NumPy, short for Numerical Python, is a fundamental package for scientific computing in Python.</li>
    <li>It provides support for arrays, matrices and a large library of high-level mathematical functions to operate on these arrays.</li>
    <li>NumPy's array object is more efficient and faster than Python's native list.</li>
    <li>It is an open-source module and is used in a wide range of applications including linear algebra, Fourier transform, and matrix computations.</li>
    <li>NumPy is also interoperable and can seamlessly and speedily integrate with a wide variety of databases.</li>
    <li>It is a key package in the field of machine learning, data analysis, and complex visualizations.</li>
    </li>
    </ul>
</ul>

## File Structure
```
.
├── Notes
    |── RohanCourse1
│   ├── AdityaCourse1
|── Other Projects
    |── Aditya
        |── NatureOrientedGeneticAlgorithm
    |── Rohan
        |── Sheakspeare Problem
|── README.md
├── ChessAI
│   ├── AI.py
│   ├── engine.py
│   ├── main.py

.
``` 
## Getting Started
### Prerequisites
<ul>
    <li>Python 3</li>
    <li>Pygame</li>
    <li>Numpy</li>
</ul>


### Installation
<ol>
    <li>Clone the repository</li>
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











