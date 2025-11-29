class ScoreBoard:
    def __init__(self):
        self.user_score = 0
        self.computer_score = 0
        self.tie_score = 0

    def update_score(self, result: str):
        
        if result == "user":
            print("You win!")
            self.user_score += 1
        elif result == "computer":
            print("Computer wins!")
            self.computer_score += 1
        else:
            print("It's a tie!")
            self.tie_score += 1

    def display_score(self):
        print("Current Score:")
        print(f"User: {self.user_score}| Computer: {self.computer_score}| Ties: {self.tie_score}")