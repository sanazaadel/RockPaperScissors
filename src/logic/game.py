import random
from src.logic.scorer import ScoreBoard

class RockPaperScissors:
    
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']
        self.winner_tuples= [('rock', 'scissors'), ('scissors', 'paper'), ('paper', 'rock')]
        self.scoreboard = ScoreBoard()
        
    def get_user_choice(self, ):
        while True:
            choice = input("Enter rock, paper, or scissors: ").strip().lower()
            if choice in self.choices:
                return choice
            print("Invalid choice. Please enter rock, paper, or scissors.")
            
    def get_computer_choice(self):
        return random.choice(self.choices)
    
    def compare_choices(self, user_choice: str, computer_choice: str):
        if user_choice == computer_choice:
            return "tie!"
        elif (user_choice, computer_choice) in self.winner_tuples:
            return "user"
        else:
            return "computer"
    
    def play(self, ):
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