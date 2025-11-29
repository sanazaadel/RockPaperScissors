# RockPaperScissors
This is a simple implementation of the classic Rock-Paper-Scissors game in Python. The game allows a user to play against the computer, which makes random choices.
## How to Play
1. Run the `main.py` script.
2. Enter your choice: rock, paper, or scissors.
3. The computer will randomly select its choice.
4. The winner will be determined based on the standard rules:
   - Rock crushes Scissors
   - Scissors cuts Paper
   - Paper covers Rock
5. After the result is displayed, you will be prompted to play again or exit the game.
## Project Structure
```
RockPaperScissors/
├── src/
│   ├── logic/
│   │   ├── game.py          # Contains the main game logic
│   │   └── scorer.py        # Manages the scoring system
│   └── main.py              # Entry point to run the game
└── README.md                # This file
```
## Requirements
- Python 3.7+
## Running the Game
To start the game, navigate to the `src` directory and run the following command:
```bash
python main.py
```
Before running the main script, ensure that PYTHONPATH is set correctly to include the `src` directory. For example, in a Unix-like terminal, you can set it as follows:
```bash
export PYTHONPATH=$(pwd)
```
Enjoy playing Rock-Paper-Scissors!  