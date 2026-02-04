from tkinter import *
from pathlib import Path
import pandas as pd

# ---------------------------- CONSTANTS ---------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
BASE_DIR = Path(__file__).resolve().parent

# ---------------------------- GLOBAL STATE ---------------------------- #
current_row = None
is_front = True          # True = German side showing, False = English side showing
flip_timer = None        # timer id for flipping to English
next_timer = None        # timer id for auto-advancing to next German


# ---------------------------- DATA LOADING ---------------------------- #
try:
    learn_df = pd.read_csv(BASE_DIR / "data" / "words_to_learn.csv")
except FileNotFoundError:
    print("Progress file not found. Loading original data.")
    learn_df = pd.read_csv(BASE_DIR / "data" / "german_words.csv")


# ---------------------------- UI SETUP ---------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

back_card_image = PhotoImage(file=str(BASE_DIR / "images" / "card_back.png"))
front_card_image = PhotoImage(file=str(BASE_DIR / "images" / "card_front.png"))

flashcard_canvas = Canvas(window, width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
flashcard_img = flashcard_canvas.create_image(400, 263, image=front_card_image)

language_title = flashcard_canvas.create_text(400, 150, fill="black", text="Deutsch", font=("Arial", 25, "italic"))
language_word = flashcard_canvas.create_text(400, 263, fill="black", text="Word", font=("Arial", 40, "bold"))

flashcard_canvas.grid(row=0, column=0, columnspan=2)


# ---------------------------- LOGIC ---------------------------- #
def _cancel_timers():
    """Cancel any pending scheduled callbacks to prevent stacking."""
    global flip_timer, next_timer
    if flip_timer is not None:
        window.after_cancel(flip_timer)
        flip_timer = None
    if next_timer is not None:
        window.after_cancel(next_timer)
        next_timer = None


def show_new_word():
    global current_row, is_front, flip_timer

    _cancel_timers()
    is_front = True

    if learn_df.empty:
        flashcard_canvas.itemconfig(language_title, text="Done!", fill="black")
        flashcard_canvas.itemconfig(language_word, text="No more words 🎉", fill="black")
        flashcard_canvas.itemconfig(flashcard_img, image=front_card_image)
        return

    current_row = learn_df.sample(1).iloc[0]

    # Show German (front)
    flashcard_canvas.itemconfig(language_title, text="Deutsch", fill="black")
    flashcard_canvas.itemconfig(language_word, text=current_row["de"], fill="black")
    flashcard_canvas.itemconfig(flashcard_img, image=front_card_image)

    # After 3 seconds, flip to English
    flip_timer = window.after(3000, flip_card)


def flip_card():
    global is_front, next_timer, flip_timer

    flip_timer = None  # this callback fired
    if current_row is None:
        return

    is_front = False

    # Show English (back)
    flashcard_canvas.itemconfig(language_title, text="English", fill="white")
    flashcard_canvas.itemconfig(language_word, text=current_row["en"], fill="white")
    flashcard_canvas.itemconfig(flashcard_img, image=back_card_image)

    # After 3 seconds on English, automatically go to next German card
    next_timer = window.after(3000, auto_next_if_english)


def auto_next_if_english():
    global next_timer
    next_timer = None
    if not is_front:
        show_new_word()


def known_word():
    """✅ If pressed anytime (German or English), remove word and go next."""
    global learn_df, current_row

    if current_row is None or learn_df.empty:
        return

    _cancel_timers()

    # Remove current word
    learn_df = learn_df.drop(current_row.name)

    # Save progress
    learn_df.to_csv(BASE_DIR / "data" / "words_to_learn.csv", index=False)

    # Next card
    show_new_word()


def wrong_word():
    """
    ❌ Behavior:
    - If on German: reveal English immediately.
    - If on English: go to next German card.
    """
    if is_front:
        flip_card()
    else:
        show_new_word()


# ---------------------------- BUTTONS ---------------------------- #
right_button_img = PhotoImage(file=str(BASE_DIR / "images" / "right.png"))
wrong_button_img = PhotoImage(file=str(BASE_DIR / "images" / "wrong.png"))

right_button = Button(image=right_button_img, highlightthickness=0, command=known_word)
right_button.grid(row=1, column=1)

wrong_button = Button(image=wrong_button_img, highlightthickness=0, command=wrong_word)
wrong_button.grid(row=1, column=0)


# ---------------------------- START ---------------------------- #
show_new_word()
window.mainloop()
