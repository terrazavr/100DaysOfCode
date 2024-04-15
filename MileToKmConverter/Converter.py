from tkinter import *

MILES = 1.60934


def button_click():
    km = int(entry_km.get())
    miles = round(km * MILES, 2)
    label_result.config(text=miles)


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=200)
window.config(padx=10, pady=30)

label_equal = Label(text="is equal to", font=("Arial", 20), pady=10)
label_equal.grid(column=0, row=1)

label_miles = Label(text="Miles", font=("Arial", 20))
label_miles.grid(column=2, row=0)

entry_km = Entry(width=5, font=("Arial", 20))
entry_km.insert(END, string="0")
entry_km.grid(column=1, row=0)

label_result = Label(text="0", font=("Arial", 20))
label_result.grid(column=1, row=1)

label_km = Label(text="Km", font=("Arial", 20))
label_km.grid(column=2, row=1)

button = Button(text="Calculate", command=button_click, pady=10)
button.grid(column=1, row=2)


window.mainloop()
