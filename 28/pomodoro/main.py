from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():

    start.config(state=NORMAL)
    reset.config(state=DISABLED)

    global reps
    reps = 0

    window.after_cancel(timer)

    canvas.itemconfig(timer_text, text="00:00")
    sessions.config(text="")
    title.config(text="Pomodoro Timer")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():

    start.config(state=DISABLED)
    reset.config(state=NORMAL)

    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    reps += 1

    if reps % 8 == 0:
        title.config(text="Long Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        title.config(text="Short Break", fg=PINK)
        count_down(short_break_sec)
    else:
        title.config(text="Study")
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    
    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        sessions.config(text=f"{tick * math.floor(reps/2)}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(bg=YELLOW)
window.minsize(width=400, height=400)
window.maxsize(width=400, height=400)

canvas = Canvas(width=200, height=224, highlightthickness=0, bg=YELLOW)
tomato_image = PhotoImage(file="28/pomodoro/tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 132, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.place(x=100, y=75)

title = Label(text="Pomodoro Timer", font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW,)
title.place(x=90, y=50)


start = Button(text="Start", font=(FONT_NAME, 25), bg=PINK, fg=GREEN, highlightthickness=0, command=start_timer)
start.place(x=70, y=350)
reset = Button(text="Reset", font=(FONT_NAME, 25), bg=PINK, fg=GREEN, highlightthickness=0, state=DISABLED, command=reset_timer)
reset.place(x=195, y=350)

tick = "✅"
sessions = Label(font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
sessions.place(x=165, y=300)



window.mainloop()