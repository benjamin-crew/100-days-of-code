import random
from tkinter import *
from tkinter.font import BOLD, ITALIC
import pandas
from random import choice
from time import sleep

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}


def is_known():
    to_learn.remove(current_card)

    df = pandas.DataFrame(to_learn)
    df.to_csv("data/words_to_learn.csv", index=False)

    generate_word()


def flip_card():
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfigure(title, text="English", fill="Black")
    canvas.itemconfigure(word, text=f'{current_card["English"]}', fill="White")


def generate_word():
    global current_card, flip_timer

    window.after_cancel(flip_timer)

    current_card = random.choice(to_learn)
    canvas.itemconfigure(title, text="Spanish", fill="Black")
    canvas.itemconfigure(word, text=f'{current_card["Spanish"]}', fill="Black")
    canvas.itemconfig(canvas_image, image=card_front_img)

    flip_timer = window.after(3000, func=flip_card)


# ---------------------------- READ CSV ------------------------------- #
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/spanish_words.csv")
finally:
    to_learn = data.to_dict(orient="records")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Cards")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
tick_img = PhotoImage(file="images/right.png")
cross_img = PhotoImage(file="images/wrong.png")

canvas = Canvas(width=800, height=526,
                bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=card_front_img)
title = canvas.create_text(
    400, 150, text="Click a button to start", font=("Ariel", 40, ITALIC))
word = canvas.create_text(400, 263, font=("Ariel", 60, BOLD))
canvas.grid(column=0, row=0, columnspan=2)

tick_button = Button(image=tick_img, highlightthickness=0, command=is_known)
cross_button = Button(
    image=cross_img, highlightthickness=0, command=generate_word)
tick_button.grid(column=0, row=1)
cross_button.grid(column=1, row=1)


flip_timer = window.after(1, func=generate_word)
window.mainloop()
