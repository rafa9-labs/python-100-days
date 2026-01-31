from tkinter import *

def fn2():
    import turtle
    tim = turtle.Turtle()
    tim.write("OBLIGATORY ARGUMENT")

# --------------------------------
# Unlimited Positional Arguments.
# --------------------------------
def multiplyInf(*args):
    m = 1
    for a in args:
        m *= a
    return m

def sumInf(*args):
    m = 0
    for a in args:
        m += a
    return m


# --------------------------------
# Unlimited Key Word Arguments.
# --------------------------------
def calculate(n, **kwargs):
    # print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs.get("add")
    n *= kwargs.get("multiply")
    print(n)
# --------------------------------  
    
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.make = kw.get("model") # The not defined params default to None.
        self.make = kw.get("cc")
        self.make = kw.get("top-speed")  
# -------------------------------

def fnTkInterModule():
    def button_clicked_show_input():
        my_label.config(text=my_input.get())

    window = Tk()
    window.title("My first GUI Program.")
    window.minsize(width=500, height=300)
    window.config(padx=100, pady=200)

    # Label
    my_label = Label(text="New text", font=("Arial", 24, "bold"))
    my_label.grid(column=0, row=0)
    my_label.config(padx=50, pady=50)
    
    # Button
    my_button = Button(text="Click me", command=button_clicked_show_input)
    my_button.grid(column=2, row=0)

    # New Button
    my_button = Button(text="Click me", command=button_clicked_show_input)
    my_button.grid(column=1, row=1)

    # Entry
    my_input = Entry(width=20)
    my_input.grid(column=3, row=2)

    window.mainloop()

    
# Tkinter has 3 ways to place objects. Pack, Place and Grid.
# Place is abotu precise positionning with x and y values. The downside is it that too specific.
# And its hard to manage.

# Grid: it images that your program is a grid. and you can 

# --------------------------------

# def button_clicked():
#     print("I got clicked!")

# So in resume the normal argument will be stored as the object is. the *args will store the objects in a tuple.
# and the **kwargs will be stored in a dict with their key and value.
    
def main():
    # fn1()
    # print(multiplyInf(2,2,2))
    # print(sumInf(2,2,2))
    # calculate(2, add=3, multiply=5)
    my_car = Car(make="Nissan")
    fnTkInterModule()

if __name__ == "__main__": 
    main()