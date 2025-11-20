import tkinter as tk
from tkinter import messagebox
import random

# Function to get computer's choice
def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

# Function to determine winner
def determine_winner(user, computer):
    if user == computer:
        return "Tie"
    elif (user == "Rock" and computer == "Scissors") or \
         (user == "Scissors" and computer == "Paper") or \
         (user == "Paper" and computer == "Rock"):
        return "You Win!"
    else:
        return "Computer Wins!"

# Function called when user makes a choice
def play(user_choice):
    global user_score, computer_score
    computer_choice = get_computer_choice()
    
    user_label.config(text=f"You chose: {user_choice}")
    computer_label.config(text=f"Computer chose: {computer_choice}")
    
    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=f"Result: {result}")
    
    if result == "You Win!":
        user_score += 1
    elif result == "Computer Wins!":
        computer_score += 1
    
    score_label.config(text=f"Score -> You: {user_score} | Computer: {computer_score}")

# Function to reset the game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_label.config(text="You chose: ")
    computer_label.config(text="Computer chose: ")
    result_label.config(text="Result: ")
    score_label.config(text="Score -> You: 0 | Computer: 0")

# Main window
root = tk.Tk()
root.title("🎮 Rock-Paper-Scissors Game 🎮")
root.geometry("450x500")
root.config(bg="#1e1e2f")

# Global scores
user_score = 0
computer_score = 0

# Title
title_label = tk.Label(root, text="Rock-Paper-Scissors", font=("Comic Sans MS", 24, "bold"), fg="#FFD700", bg="#1e1e2f")
title_label.pack(pady=20)

# User and Computer choice labels
user_label = tk.Label(root, text="You chose: ", font=("Arial", 16), fg="#00FFFF", bg="#1e1e2f")
user_label.pack(pady=10)

computer_label = tk.Label(root, text="Computer chose: ", font=("Arial", 16), fg="#FF69B4", bg="#1e1e2f")
computer_label.pack(pady=10)

# Result label
result_label = tk.Label(root, text="Result: ", font=("Arial", 18, "bold"), fg="#7CFC00", bg="#1e1e2f")
result_label.pack(pady=20)

# Buttons for choices
button_frame = tk.Frame(root, bg="#1e1e2f")
button_frame.pack(pady=20)

rock_button = tk.Button(button_frame, text="Rock", font=("Arial", 14, "bold"), width=10, bg="#FF4500", fg="white", command=lambda: play("Rock"))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, text="Paper", font=("Arial", 14, "bold"), width=10, bg="#1E90FF", fg="white", command=lambda: play("Paper"))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(button_frame, text="Scissors", font=("Arial", 14, "bold"), width=10, bg="#32CD32", fg="white", command=lambda: play("Scissors"))
scissors_button.grid(row=0, column=2, padx=10)

# Score label
score_label = tk.Label(root, text="Score -> You: 0 | Computer: 0", font=("Arial", 16), fg="#FFD700", bg="#1e1e2f")
score_label.pack(pady=20)

# Reset button
reset_button = tk.Button(root, text="Reset Game", font=("Arial", 14, "bold"), bg="#FF1493", fg="white", command=reset_game)
reset_button.pack(pady=20)

footer = tk.Label(root, text="✨ Designed by Aryan Kumar", font=("Poppins", 10), bg="#355B69", fg="white")
footer.pack(side="bottom", pady=10)

root.mainloop()
