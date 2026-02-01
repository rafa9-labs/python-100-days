
# ---------------------------- CONSTANTS ------------------------------- 
from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
# work_reps = 0
# pause_reps = 0 # Big break every 3 cycles.
    
# work_sec = 60 * WORK_MIN
# pause_reps = 60 * SHORT_BREAK_MIN
# pause_reps = 60 * LONG_BREAK_MIN
    
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    
    reps += 1
    
    work_sec = 60 * WORK_MIN
    short_pause_sec = 60 * SHORT_BREAK_MIN
    big_pause_sec = 60 * LONG_BREAK_MIN
        
    if reps % 8 == 0:
        countdown(big_pause_sec)
        state_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_pause_sec)
        state_label.config(text="Short Break", fg=PINK)
        current_marks = checkmark_label.cget("text")
        checkmark_label.config(text=current_marks + "✔")
    else:
        countdown(work_sec)
        state_label.config(text="Work", fg=GREEN)


def next_timer():
    return

def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    state_label.config(text="Timer")
    checkmark_label.config(text="")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
# import time

# count = 5
# while True:
#     time.sleep(1)
#     count -= 1
#     print(count)

def countdown(count):
    minutes, seconds = divmod(count, 60)
    
    # Same as this.
    # minutes = count // 60
    # seconds = count % 60

    timer_text_value = f"{minutes:02d}:{seconds:02d}"
    canvas.itemconfig(timer_text, text=timer_text_value)

    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=20, pady=20, bg=YELLOW)
window.resizable(False, False)


# def say_something(a,b,c):
#     print(a)
#     print(b)
#     print(c)

# window.after(1000, say_something, 3,5,6)

tomato_img = PhotoImage(file="day_28_tkinter_dynamic_typing/pomodoro-start/tomato.png")

# Canvas definition with Timer and Image.
canvas = Canvas(window,
                width=200,
                height=224,
                bg=YELLOW,
                highlightthickness=0)
canvas.grid(column=1, row=1)
canvas.create_image(100, 112, image=tomato_img)

timer_text = canvas.create_text(100, 130,
                                text="00:00",
                                fill="white",
                                font=("Courier", 35, "bold"))

# State Label
state_label = Label(
    text="Timer",
    fg=GREEN,
    font=(FONT_NAME, 40, "bold"),
    bg=YELLOW,
    width=10
)
state_label.grid(column=1, row=0)

# Checkmark symbol
checkmark_label = Label(text="",
                        fg=GREEN,
                        font=(FONT_NAME, 15, "bold"),
                        bg=YELLOW)
checkmark_label.grid(column=1, row=3, pady=(10,0))

# Start button
start_button = Button(text="Start",
                        fg="black", font=(FONT_NAME, 15, "bold"),
                        bg="white", highlightthickness=0,
                        command=start_timer)
start_button.grid(column=0, row=4, pady=(10,0))

# Reset button
reset_button = Button(text="Reset",
                        fg="black",
                        font=(FONT_NAME, 15, "bold"),
                        bg="white",
                        highlightthickness=0,
                        command=reset_timer)
reset_button.grid(column=1, row=4, pady=(10,0))

# Next button
next_button = Button(text="Next",
                        fg="black",
                        font=(FONT_NAME, 15, "bold"),
                        bg="white", highlightthickness=0,
                        command=start_timer)
next_button.grid(column=2, row=4, pady=(10,0))


window.mainloop()