"""
Author: Sanaz Adel
Description: Main logic for rock paper scissors game
"""
    
import random
from src.logic.scorer import ScoreBoard
from typing import Tuple,   List


class RockPaperScissors:
    """Main class for rock paper scissors game"""
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']
        self.winner_tuples = [('rock', 'scissors'), ('scissors', 'paper'), ('paper', 'rock')]
        self.scoreboard = ScoreBoard()
        
    def get_user_choice(self, ) -> str:
        while True:
            choice = input("Enter rock, paper, or scissors: ").strip().lower()
            if choice in self.choices:
                return choice
            print("Invalid choice. Please enter rock, paper, or scissors.")
            
    def get_computer_choice(self)-> str:
        """Get computer's random choice from list of choices"""
        return random.choice(self.choices)
    
    def compare_choices(self, user_choice: str, computer_choice: str)-> str:
        """Decide the winner of the game based on user and computer choises

        :param user_choice: the user's choice
        :param computer_choice: the computer's choice
        :return: the result of the game (who won: "user", "computer", or "tie")
        """
        if user_choice == computer_choice:
            return "tie!"
        elif (user_choice, computer_choice) in self.winner_tuples:
            return "user"
        else:
            return "computer"
    
    def play(self, ):
        """
        - Get user's choice
        - Get computer's choice
        - Decide the winner
        - Update the scoreboard
        - Asking whether replay or not
        """
        user_choice = self.get_user_choice()
        computer_choice = self.get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        result = self.compare_choices(user_choice, computer_choice)
        self.scoreboard.update_score(result)
        self.scoreboard.display_score()
        replay = input("Thanks for playing! Do you want to play again? (y/n): ")
        if replay.lower() == 'y':   
            self.play()         
        else:
            print("Goodbye!")