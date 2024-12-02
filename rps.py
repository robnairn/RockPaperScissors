from tkinter import *
from random import randint
from tkinter import ttk

# Make window
window = Tk()
window.title('Rock Paper Scissors')
window.geometry('600x700')
window.config(bg='white')

# Images
rps = PhotoImage(file = 'rps.png')
rock = PhotoImage(file = 'rock.png')
paper = PhotoImage(file = 'paper.png')
scissors = PhotoImage(file = 'scissors.png')

# add images to a list
image_list = [rock, paper, scissors]

# Put image on screen
image_label = Label(window, image = rps)
image_label.pack(pady=10)

def spin():
    computer_choice = randint(0,2)
    image_label.config(image = image_list[computer_choice])
    
    # turn player choice into number
    if player_choice.get() == 'Rock':
        player_choice_value = 0
    elif player_choice.get() == 'Paper':
        player_choice_value = 1
    elif player_choice.get() == 'Scissors':
        player_choice_value = 2
     
    # player picks Rock
    if player_choice_value == 0: #rock
        if computer_choice == 0: #rock
            result_label.config(text="It's a Draw")
        elif computer_choice == 1: #paper
            result_label.config(text="Paper covers rock - You loser!! hahahaha")
        elif computer_choice == 2: #scissors
            result_label.config(text="Rock smashes scissors - Winner!!!!")
            
    # player picks Paper
    if player_choice_value == 1: #paper
        if computer_choice == 1: #paper
            result_label.config(text="It's a Draw")
        elif computer_choice == 2: #scissors
            result_label.config(text="Sicsors cuts paper - You loser!! hahahaha")
        elif computer_choice == 0: #rock
            result_label.config(text="Paper covers rock - Winner!!!!")
            
    # player picks Scissors
    if player_choice_value == 2: #scissors
        if computer_choice == 2: #scissors
            result_label.config(text="It's a Draw")
        elif computer_choice == 1: #paper
            result_label.config(text="Scissors cut paper - Winner")
        elif computer_choice == 0: #rock
            result_label.config(text="Rock smashes scissors - You loser!! hahahaha")

# Combo box
player_choice = ttk.Combobox(window, value=('Rock', 'Paper', 'Scissors'))
player_choice.current(0)
player_choice.pack(pady=10)

# spin button
spin_button = Button(window, text='Spin!!', command=spin)
spin_button.pack(pady=10)

# results
result_label = Label(window, text='', font=('arial, 16'))
result_label.pack(pady=40)

window.mainloop()