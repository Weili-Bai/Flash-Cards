from tkinter import *

import pandas

import French_words

BACKGROUND_COLOUR = "#B1DDC6"
SMALL_FONT = ("Ariel", 40, "italic")
BIG_FONT = ("Ariel", 60, "bold")
PADDING = 50
WORD_TUPLE = {}


def change_word():
    global WORD_TUPLE, flip_delay
    window.after_cancel(flip_delay)
    canvas.itemconfig(card_image, image=front_image)
    canvas.delete("title")
    canvas.create_text(400, 150, text="French", font=SMALL_FONT, tag="title")
    canvas.delete("word")
    WORD_TUPLE = French_words.get_tuple()
    canvas.create_text(400, 263, text=WORD_TUPLE["French"], font=BIG_FONT, tag="word")
    flip_delay = window.after(3000, flip_card)


def flip_card():
    global WORD_TUPLE
    canvas.itemconfig(card_image, image=back_image)
    canvas.delete("title")
    canvas.create_text(400, 150, text="English", font=SMALL_FONT, tag="title", fill="white")
    canvas.delete("word")
    canvas.create_text(400, 263, text=WORD_TUPLE["English"], font=BIG_FONT, tag="word", fill="white")


def update_file():
    global WORD_TUPLE
    if WORD_TUPLE != {}:
        French_words.my_dict.remove(WORD_TUPLE)
        frame = pandas.DataFrame(French_words.my_dict)
        frame.to_csv("./data/words_to_learn.csv", index=False)
    else:
        pass


def check_mark():
    global WORD_TUPLE
    if WORD_TUPLE != French_words.SUCCESS:
        update_file()
        change_word()
    else:
        pass


def do_nothing():
    pass


window = Tk()
window.title("Flash Cards")
window.config(padx=PADDING, pady=PADDING, bg=BACKGROUND_COLOUR)
flip_delay = window.after(500, do_nothing)
canvas = Canvas(width=800, height=526)
front_image = PhotoImage(file="./images/card_front.png")
back_image = PhotoImage(file="./images/card_back.png")
card_image = canvas.create_image(400, 263, image=front_image)
canvas.grid(columnspan=2, row=0, column=0)
canvas.config(bg=BACKGROUND_COLOUR, highlightthickness=0)
cross_image = PhotoImage(file="./images/wrong.png")
cross_button = Button()
cross_button.config(image=cross_image, highlightthickness=0, command=change_word)
cross_button.grid(row=1, column=0)
check_image = PhotoImage(file="./images/right.png")
check_button = Button()
check_button.config(image=check_image, highlightthickness=0, command=check_mark)
check_button.grid(row=1, column=1)
canvas.create_text(400, 150, text="title", font=SMALL_FONT, tag="title")
canvas.create_text(400, 263, text="type", font=BIG_FONT, tag="word")
window.mainloop()
