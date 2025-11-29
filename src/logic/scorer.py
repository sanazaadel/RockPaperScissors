class ScoreBoard:
    """General class for keeping and displaying the score of the game
    """
    
    def __init__(self):
        self.user_score = 0
        self.computer_score = 0
        self.tie_score = 0

    def update_score(self, result: str):
        """Update the score based on the result of the game

        :param result: who already won:"user", "computer" or "tie"
        :type result: corresponging score will be updated
        """
        
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
        """Display the current score of the game on the board like "User: x | Computer: y | Ties: z"
        """
        
        print("Current Score:")
        print(f"User: {self.user_score}| Computer: {self.computer_score}| Ties: {self.tie_score}")