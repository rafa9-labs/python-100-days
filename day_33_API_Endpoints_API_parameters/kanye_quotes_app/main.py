import requests
from tkinter import Tk, Canvas, PhotoImage, Button
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
print(BASE_DIR)

window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(window, width=300, height=414, highlightthickness=0)
background_img = PhotoImage(file=str(BASE_DIR / "background.png"))
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(
    150, 207,
    text="Kanye Quote Goes HERE",
    width=250,
    font=("Arial", 30, "bold"),
    fill="white"
)
canvas.grid(row=0, column=0)

def get_quote(c, text_id):
    r = requests.get("https://api.kanye.rest/", timeout=10)
    r.raise_for_status()
    quote = r.json()["quote"]
    c.itemconfig(text_id, text=quote)

kanye_img = PhotoImage(file=str(BASE_DIR / "kanye.png"))
kanye_button = Button(      
    image=kanye_img,
    highlightthickness=0,
    command=lambda: get_quote(canvas, quote_text)
)
kanye_button.grid(row=1, column=0)

get_quote(canvas, quote_text)

window.mainloop()
