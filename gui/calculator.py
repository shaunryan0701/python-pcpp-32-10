import tkinter as tk
from tkinter import messagebox

def evaluate():
    operator = operator_var.get()
    operand_1 = int(num1_text.get())
    operand_2 = int(num2_text.get())
    result = 0
    if operator == 1:
        result = operand_1 + operand_2
    elif operator == 2:
        result = operand_1 - operand_2
    elif operator == 3:
        result = operand_1 * operand_2
    else:
        result = operand_1 / operand_2

    messagebox.showinfo(title="Ahhhh", message=str(result))

window = tk.Tk()
window.title("Calculator")
operator_var = tk.IntVar()
plus = tk.Radiobutton(window, variable=operator_var, text="+", value=1)
plus.grid(row=0, column=1)
minus = tk.Radiobutton(window, variable=operator_var, text="-", value=2)
minus.grid(row=1, column=1)

num1_text = tk.StringVar()
num2_text = tk.StringVar()

num1 = tk.Entry(window, textvariable=num1_text)
num1.grid(row=2, column=0)
num2 = tk.Entry(window, textvariable=num2_text)
num2.grid(row=2, column=2)

multiply = tk.Radiobutton(window, variable=operator_var, text="*", value=3)
multiply.grid(row=2, column=1)
divide = tk.Radiobutton(window, variable=operator_var, text="/", value=4)
divide.grid(row=3, column=1)

eval = tk.Button(text="Evaluate", command=evaluate)
eval.grid(row=4, column=1)
window.mainloop()