import tkinter as tk
from tkinter import Text

calculation = ""



def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)


def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")
        pass

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")


root = tk.Tk()
root.geometry("300x275")
root.mainloop()

text_result: tk.Text(root, height=2, width=16, font=("Arial, 24"))
text_result.grid(columnspan=5)

btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), widht=5, font=("Arial", 14))
btn_1.grid(row=2, column=1)
btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), widht=5, font=("Arial", 14))
btn_2.grid(row=2, column=2)
btn_3 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), widht=5, font=("Arial", 14))
btn_3.grid(row=2, column=2)
root.mainloop()