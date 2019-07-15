import tkinter as tk
from model import calc

def calculate():
    """Calculates weights and sets message."""
    STANDARD_BAR = 45
    STANDARD_PLATES = [45,25,10,5,2.5]
    try:
        bar_weight = STANDARD_BAR
        plate_list = STANDARD_PLATES
        try:
            lift_weight = float(entry_weight.get())
        except ValueError:
            message.config('Lift weight must be a number.')
            return
        if entry_bar.get() != '':
            try:
                bar_weight = float(entry_bar.get())
            except ValueError:
                message.config('Bar weight must be a number.')
                return
        if entry_plates.get() != '':
            try:
                plate_list = calc.get_list(entry_plates.get())
            except TypeError:
                message.config('Plates mus be comma separated numbers.')
                return
        plate_dict = calc.get_plates(lift_weight, bar_weight, plate_list)
        message.config(text=str(plate_dict))
    except calc.LessThanBar:
        message.config(text='Your lift weight is less than the bar.')
    except calc.NotDivisible:
        message.config(text='Your lift weight is not divisible by your plates')

m = tk.Tk()
m.attributes('-type', 'dialog')
m.title("Plate Calculator")
label_message = tk.Label(m, text='Add to each end:')
label_message.grid(row=1, column=1)
message = tk.Label(m, text='Enter weight to calculate')
message.grid(row=1, column=2)
label_weight = tk.Label(m, text='Enter weight to lift:')
label_weight.grid(row=2, column=1)
entry_weight = tk.Entry(m)
entry_weight.grid(row=2, column=2)
label_bar = tk.Label(m, text='(Opt) Bar weight:')
label_bar.grid(row=3, column=1)
entry_bar = tk.Entry(m)
entry_bar.grid(row=3, column=2)
label_plates = tk.Label(m, text='(Opt) Enter plate weights "1,2,3":')
label_plates.grid(row=4, column=1)
entry_plates = tk.Entry(m)
entry_plates.grid(row=4, column=2)
button_calc = tk.Button(m, text='Calculate', command=calculate)
button_calc.grid(row=5, column=1)
button_exit = tk.Button(m, text='Exit', command=m.destroy)
button_exit.grid(row=5, column=2)

m.mainloop()

