from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}
current_card = {}

try:
    data = pd.read_csv("word_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("french_words.csv")
    to_learn = data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("word_to_learn.csv", index=False)
    next_card()


def next_card():
    global current_card, flip_timer

    window.after_cancel(flip_timer)

    current_card = random.choice(to_learn)
    # The itemconfig helps to change an item on a canvas
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_text, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_image)

    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_background, image=flip_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_text, text=current_card["English"], fill="white")

# Creating a GUI window
window = Tk()
window.title("FLASH CARD APP")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# This function helps to change the card after 3 seconds
flip_timer = window.after(3000, func=flip_card)

# The canvas allow objects overlay. Here is how to set up a canvas
canvas = Canvas(width=800, height=526)

# The code below shows how image can be added to a canvas
flip_image = PhotoImage(file="card_back.png")
card_image = PhotoImage(file="card_front.png")
card_background = canvas.create_image(400, 263, image=card_image)

# This shows us how a text can be inserted on a canvas
card_title = canvas.create_text(400, 150, text="Title", font=("Arial",40,"italic"))
card_text = canvas.create_text(400, 263, text="WORD", font=("Arial",60,"bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


# Adding button in tkinter

# Adding the right button
tick_image = PhotoImage(file="right.png")
right_button = Button(image=tick_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=0)

# Adding the wrong button
cross_image = PhotoImage(file="wrong.png")
wrong_button = Button(image=cross_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=1)


next_card()

window.mainloop()

