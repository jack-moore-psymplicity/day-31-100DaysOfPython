from tkinter import *
import pandas as pd
from random import shuffle, choice
import time

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- WORD LIST ------------------------------- #
current_card = {}
to_learn = {}

try:
    data = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pd.read_csv('data/spanish_words.csv')
    original_data['Score'] = 1
    data = original_data.head(100)
    to_learn = original_data.to_dict(orient = 'records')
else:
    data = data.head(100)
    to_learn = data.to_dict(orient = 'records')


# ---------------------------- FUNCTIONS ------------------------------- #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    print(current_card)
    canvas.itemconfig(card_title, text= 'Espanol', fill = 'black')
    canvas.itemconfig(card_spanish, text= current_card['Spanish'], fill = 'black')
    canvas.itemconfig(card_side, image = front_img)
    flip_timer = window.after(3000, flip_card)


def right_card():
    global current_card, to_learn
    current_card['Score'] *= 2
    data = pd.DataFrame(to_learn)
    data = data.sort_values(by = ['Score'])
    data.to_csv('data/words_to_learn.csv', index=False)
    next_card()
def wrong_card():
    global current_card, to_learn
    current_card['Score'] *= 0.75
    data = pd.DataFrame(to_learn)
    data = data.sort_values(by = ['Score'])
    data.to_csv('data/words_to_learn.csv', index=False)
    next_card()

def flip_card():
    canvas.itemconfig(card_side, image = back_img)
    canvas.itemconfig(card_spanish, text= current_card['English'], fill = 'white')
    canvas.itemconfig(card_title, text= 'English', fill = 'white')

# ---------------------------- UI SETUP  ------------------------------- #
window = Tk()
window.title('Destello')
window.config(padx=50, pady=50, bg = BACKGROUND_COLOR)


canvas = Canvas(width = 800, height = 526)
back_img = PhotoImage(file="images/card_back.png")
front_img = PhotoImage(file="images/card_front.png")
card_side = canvas.create_image(400, 263, image=front_img)
card_title = canvas.create_text(400, 150, text = "Espanol", font =("Ariel", 40, "italic"))
card_spanish = canvas.create_text(400, 300, text = '', font =("Ariel", 50, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0,column=0, columnspan=2)

flip_timer = window.after(3000, func=flip_card)

right_img = PhotoImage(file="images/right.png")
button_right = Button(image=right_img, bg=BACKGROUND_COLOR, highlightthickness=0, command = wrong_card)
button_right.grid(row=1, column=0)

wrong_img = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=wrong_img, bg=BACKGROUND_COLOR, highlightthickness=0, command = right_card)
button_wrong.grid(row=1, column=1)

data = data.head(50)
to_learn = data.to_dict(orient = 'records')
print(current_card)
print(to_learn[0:9])
next_card()

mainloop()