from tkinter import *

CONVERSION_RATE = 1.60934

def main():
    
    def calculateKm():
        try:
            miles = float(user_insert.get().strip())
        except ValueError:
            km_label.config(text="0.00")   # or "Invalid"
            return

        km = miles * CONVERSION_RATE
        km_label.config(text=f"{km:.2f}")

    
    window = Tk()
    window.title("Miles to km converter.")
    window.minsize(width=300, height=200)
    window.config(padx=20, pady=20)
    
    # Input 1
    user_insert =  Entry()
    user_insert.grid(column=1, row=0, ipady=10)
    
    # Label 1
    miles_label =  Label(text="Miles", font=("Arial", 24, "normal"))
    miles_label.grid(column=2, row=0)
    
    
    # Label 2
    isequal_label =  Label(text="is equal to", font=("Arial", 24, "normal"))
    isequal_label.grid(column=0, row=1)
    
    # Label 3
    km_label =  Label(text="0", font=("Arial", 24, "normal"))
    km_label.grid(column=1, row=1)
    
    # Label 4
    km_num_label =  Label(text="Km", font=("Arial", 24, "normal"))
    km_num_label.grid(column=2, row=1)
    
    # Button 1
    km_num_label =  Button(text="Calculate", font=("Arial", 24, "normal"), command=calculateKm)
    km_num_label.grid(column=1, row=2)
    
    window.mainloop()

if __name__ == "__main__": 
    main()