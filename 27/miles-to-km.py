from tkinter import *

FONT = "Courier"
FONTSIZE = 14

def button_clicked():
    miles = float(input.get())
    km = float(miles * 1.609)
    answer_label.config(text="{:.2f}".format(km))


### GUI Layout
window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=150, height=100)
window.config(padx=20, pady=20)

input = Entry(width=10)
input.grid(column=2, row=0)

miles_label = Label(text="Miles",font=(FONT, FONTSIZE))
miles_label.grid(column=3, row=0)

is_equal_to_label = Label(text="is equal to", font=(FONT, FONTSIZE))
is_equal_to_label.grid(column=0, row=1)

answer_label = Label(text="",font=(FONT, FONTSIZE))
answer_label.grid(column=2, row=1)

km_label = Label(text="is equal to", font=(FONT, FONTSIZE))
km_label.grid(column=3, row=1)

button = Button(text="Calculate", font=(FONT, FONTSIZE), command=button_clicked)
button.grid(column=2, row=3)



window.mainloop()