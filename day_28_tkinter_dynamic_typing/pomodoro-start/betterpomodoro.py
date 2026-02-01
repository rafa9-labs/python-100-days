from tkinter import *
from enum import Enum, auto

# ---------------------------- CONSTANTS ------------------------------- #
PINK   = "#e2979c"
RED    = "#e7305b"
GREEN  = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- STATE MODEL ------------------------------ #
class SessionState(Enum):
    IDLE = auto()
    WORK = auto()
    SHORT_BREAK = auto()
    LONG_BREAK = auto()

reps = 0                 # counts sessions (work + breaks)
timer_id = None          # stores the after() callback id
state = SessionState.IDLE

# ---------------------------- TIMER CONTROL ---------------------------- #
def start_timer():
    """Start or continue the pomodoro cycle."""
    _start_next_session()

def next_timer():
    global reps, state
    _cancel_timer()

    # If idle, start normally (don’t “skip”)
    if state == SessionState.IDLE:
        start_timer()
        return

    _start_next_session()

def reset_timer():
    """Reset everything back to the initial UI."""
    global reps, state
    _cancel_timer()
    reps = 0
    state = SessionState.IDLE

    canvas.itemconfig(timer_text, text="00:00")
    state_label.config(text="Timer", fg=GREEN)
    checkmark_label.config(text="")

def _start_next_session():
    """Advance reps and start the correct session based on pomodoro rules."""
    global reps, state

    reps += 1

    work_sec        = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec  = LONG_BREAK_MIN * 60

    # Pomodoro logic:
    # 1) Every 8th session = long break
    # 2) Every even session (except 8th) = short break
    # 3) Every odd session = work
    if reps % 8 == 0:
        state = SessionState.LONG_BREAK
        _set_state_ui("Long Break", RED)
        _countdown(long_break_sec)

    elif reps % 2 == 0:
        state = SessionState.SHORT_BREAK
        _set_state_ui("Short Break", PINK)
        _countdown(short_break_sec)
        
    else:
        state = SessionState.WORK
        _set_state_ui("Work", GREEN)
        _countdown(work_sec)

def _set_state_ui(title: str, color: str):
    state_label.config(text=title, fg=color)

def _add_checkmark():
    current = checkmark_label.cget("text")
    checkmark_label.config(text=current + "✔")

def _cancel_timer():
    global timer_id
    if timer_id is not None:
        window.after_cancel(timer_id)
        timer_id = None

def _countdown(count):
    global timer_id, state

    minutes, seconds = divmod(count, 60)
    canvas.itemconfig(timer_text, text=f"{minutes:02d}:{seconds:02d}")

    if count > 0:
        timer_id = window.after(1000, _countdown, count - 1)
    else:
        timer_id = None

        # ✅ Add a checkmark when a WORK session completes
        if state == SessionState.WORK:
            _add_checkmark()

        _start_next_session()


# ---------------------------- UI SETUP -------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=20, pady=20, bg=YELLOW)
window.resizable(False, False)

tomato_img = PhotoImage(file="day_28_tkinter_dynamic_typing/pomodoro-start/tomato.png")

canvas = Canvas(window, width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.grid(column=1, row=1)
canvas.create_image(100, 112, image=tomato_img)

timer_text = canvas.create_text(
    100, 130,
    text="00:00",
    fill="white",
    font=(FONT_NAME, 35, "bold")
)

state_label = Label(
    text="Timer",
    fg=GREEN,
    bg=YELLOW,
    font=(FONT_NAME, 40, "bold"),
    width=10  # keep the window stable
)
state_label.grid(column=1, row=0)

checkmark_label = Label(
    text="",
    fg=GREEN,
    bg=YELLOW,
    font=(FONT_NAME, 15, "bold")
)
checkmark_label.grid(column=1, row=3, pady=(10, 0))

# ---------------------------- BUTTON STYLING --------------------------- #
def make_button(text, command, bg, fg="white"):
    return Button(
        text=text,
        command=command,
        font=(FONT_NAME, 14, "bold"),
        bg=bg,
        fg=fg,
        activebackground=bg,
        activeforeground=fg,
        highlightthickness=0,
        bd=0,
        padx=14,
        pady=6,
        cursor="hand2"
    )

start_button = make_button("Start", start_timer, bg=GREEN, fg="black")
start_button.grid(column=0, row=4, pady=(12, 0), padx=8)

reset_button = make_button("Reset", reset_timer, bg=RED, fg="white")
reset_button.grid(column=1, row=4, pady=(12, 0), padx=8)

next_button = make_button("Next", next_timer, bg=PINK, fg="black")
next_button.grid(column=2, row=4, pady=(12, 0), padx=8)

window.mainloop()
