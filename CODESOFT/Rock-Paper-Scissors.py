import random
import tkinter as tk

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    user_choice = user_choice_var.get()
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=f"You chose {user_choice}.\nComputer chose {computer_choice}.\n{result}")

# Create the main window
window = tk.Tk()
window.title("Rock-Paper-Scissors Game")

# Create a label for instructions
instructions_label = tk.Label(window, text="Select your choice:")
instructions_label.pack()

# Create radio buttons for user choice
user_choice_var = tk.StringVar()
user_choice_var.set("rock")  # Default choice
rock_radio = tk.Radiobutton(window, text="Rock", variable=user_choice_var, value="rock")
paper_radio = tk.Radiobutton(window, text="Paper", variable=user_choice_var, value="paper")
scissors_radio = tk.Radiobutton(window, text="Scissors", variable=user_choice_var, value="scissors")

rock_radio.pack()
paper_radio.pack()
scissors_radio.pack()

# Create a "Play" button
play_button = tk.Button(window, text="Play", command=play_game)
play_button.pack()

# Create a label for displaying the result
result_label = tk.Label(window, text="")
result_label.pack()

# Start the GUI main loop
window.mainloop()
