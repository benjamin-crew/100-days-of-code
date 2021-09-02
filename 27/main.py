from tkinter import *

# Layout Managers
# Pack, Place, Grid
# Pack is used to just add a widget in the next available spot
# Place allows you to place your widget at x, y. my_label.place(x=0, y=0)
# Grid allows you to define your window into rows, columns. my_label.grid(column=0, row=0)
# Grid is relative to other components. I.e if you only have one widget, and you set it to column=5, row=5, it will appear at =0, =0

def button_clicked():
    my_label.config(text="Button got clicked")
    text = input.get()
    print(text)
    print("I got clicked")



window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Create Label
my_label = Label(text="I am a label.", font=("Arial", 14, "bold"))
# Display Label
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Updating the label
my_label["text"] = "new text"
my_label.config(text="Even newer label")

# Create Button
button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

# Entry
input = Entry(width=10)
input.grid(column=2, row=2)



window.mainloop()
