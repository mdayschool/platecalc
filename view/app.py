import tkinter as tk
from model import calc

def calculate():
    """Calculates weights and sets message."""
    message.config(text=str(calc.get_plates(float(weight.get()))))

m = tk.Tk()
m.attributes('-type', 'dialog')
m.title("Plate Calculator")
message = tk.Label(m, text='Enter weight to calculate')
message.grid(row=1)
weight = tk.Entry(m)
weight.grid(row=2)
calc_button = tk.Button(m, text='Calculate', command=calculate)
calc_button.grid(row=3)
exit_button = tk.Button(m, text='Exit', command=m.destroy)
exit_button.grid(row=4)

m.mainloop()

