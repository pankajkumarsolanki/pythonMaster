import random


class GuessingGame():

    def __init__(self):
        self.rand_choice = random.randint(0,10)

    def reset_random(self):
        print("Resetting Random Choice")
        self.rand_choice = random.randint(0,10)

    def guess(self):
        user_guess = int(input("Please input your guess (0-10): "))
        if user_guess == self.rand_choice:
            print("Correct Guess!")
        else:
            print("Sorry you didn't guess correctly!")
            if user_guess<self.rand_choice:
                print("Guess Higher")
            else:
                print("Guess Lower")
            print("Call the guess() method again to try again.")



g = GuessingGame()
g.rand_choice
g.reset_random()
g.guess()