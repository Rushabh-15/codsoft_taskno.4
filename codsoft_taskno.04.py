from tkinter import *
import random

class RockPaperScissorsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors Game")
        self.root.geometry("500x500")
        self.root.config(bg = "darkturquoise")

        self.user_score = 0
        self.computer_score = 0

        self.label = Label(root, text="Rock, Paper, Scissors", font=("Arial", 20), bg = "#FF9912")
        self.label.pack(pady=20)

        self.rock_button = Button(root, text="Rock", width=10, height=2, command=lambda: self.play("Rock"), font=("Arial", 12), bg = "lawngreen")
        self.paper_button = Button(root, text="Paper", width=10, height=2, command=lambda: self.play("Paper"), font=("Arial", 12), bg = "lawngreen")
        self.scissors_button = Button(root, text="Scissors", width=10, height=2, command=lambda: self.play("Scissors"), font=("Arial", 12), bg = "lawngreen")

        self.rock_button.pack(pady=5)
        self.paper_button.pack(pady=5)
        self.scissors_button.pack(pady=5)

        self.user_choice_label = Label(root, text="", font=("Arial", 20))
        self.computer_choice_label = Label(root, text="", font=("Arial", 20))
        self.user_choice_label.pack(pady=5)
        self.computer_choice_label.pack()

        self.result_label = Label(root, text="", font=("Arial", 20))
        self.result_label.pack(pady=10)

        self.score_label = Label(root, text="User: 0 | Computer: 0", font=("Arial", 20))
        self.score_label.pack()

    def play(self, user_choice):
        choices = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(choices)

        self.user_choice_label.config(text=f"Your choice: {user_choice}")
        self.computer_choice_label.config(text=f"Computer's choice: {computer_choice}")

        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (
            (user_choice == "Rock" and computer_choice == "Scissors")
            or (user_choice == "Paper" and computer_choice == "Rock")
            or (user_choice == "Scissors" and computer_choice == "Paper")
        ):
            result = "You win!"
            self.user_score += 1
        else:
            result = "Computer wins!"
            self.computer_score += 1

        self.score_label.config(text=f"User: {self.user_score} | Computer: {self.computer_score}")

        self.result_label.config(text=result)

if __name__ == "__main__":
    root = Tk()
    app = RockPaperScissorsApp(root)
    root.mainloop()
