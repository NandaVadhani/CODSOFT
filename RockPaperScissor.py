import tkinter as tk
import random
def determine_winner(player_choice):
    choices = ['Rock', 'Paper', 'Scissor']
    computer_choice = random.choice(choices)
    computer_response.set(f"Computer's response: {computer_choice}")
    
    if player_choice == computer_choice:
        result.set("It's a tie!")
    elif (player_choice == 'Rock' and computer_choice == 'Scissor') or \
         (player_choice == 'Paper' and computer_choice == 'Rock') or \
         (player_choice == 'Scissor' and computer_choice == 'Paper'):
        result.set("You win!")
    else:
        result.set("You lose!")

root = tk.Tk()
root.title("Rock Paper Scissor Game")
root.geometry("500x300")

frame = tk.Frame(root)
frame.pack(pady=20)

user_choice_label = tk.Label(frame, text="User choice:", font=("Helvetica", 14))
user_choice_label.pack(side=tk.LEFT, padx=20)
button_font = ("Helvetica", 14)
rock_button = tk.Button(frame, text="Rock", font=button_font, command=lambda: determine_winner('Rock'))
rock_button.pack(side=tk.LEFT, padx=20)

paper_button = tk.Button(frame, text="Paper", font=button_font, command=lambda: determine_winner('Paper'))
paper_button.pack(side=tk.LEFT, padx=20)

scissor_button = tk.Button(frame, text="Scissor", font=button_font, command=lambda: determine_winner('Scissor'))
scissor_button.pack(side=tk.LEFT, padx=20)
computer_response = tk.StringVar()
computer_label = tk.Label(root, textvariable=computer_response, font=("Helvetica", 14))
computer_label.pack(pady=20)

result = tk.StringVar()
result_label = tk.Label(root, textvariable=result, font=("Helvetica", 14))
result_label.pack(pady=20)
root.mainloop()