import tkinter as tk

def add_digit(digit):
    Value = calc.get()
    if Value[0] == "0" and len(Value) == 1:
        Value = Value[1:]
    calc.delete(0, tk.END)
    calc.insert(0,Value+digit)

def add_operation(operation):
    Value = calc.get()

    if Value[-1] in "+, -, * ,/, .":
        Value = Value[:-1]

    if Value[-1] in "**":
        Value = Value[:-1]

    if Value[-1] in "//":
        Value = Value[:-1]

    calc.delete(0, tk.END)
    calc.insert(0,(Value+operation))

def calculate():
    try:
        Value = calc.get()
        if Value[-1] in ".":
            Value = Value[:-1]
        elif Value[-1] in "**, //":
            Value = Value[:-2]
        elif Value[-1] in "+, -, *, /":
            Value = Value[:-1]

        calc.delete(0, tk.END)
        calc.insert(0,eval(Value))
    except:
        pass

def clear():
    calc.delete(0, tk.END)
    calc.insert(0,0)

def clear_one():
    Value = calc.get()
    try:
        if Value[1]:
            calc.delete(calc.index(tk.END) - 1)
            raise IndexError
    except:
        pass

def make_digit_button(digit):
    return tk.Button(text=digit, bd=5, font=("Arial", 15), command=lambda : add_digit(digit))


def make_operation_button(operation):
    return tk.Button(text=operation, bd=5, font=("Arial", 15), fg="red", command=lambda : add_operation(operation))

def make_calc_button(operation):
    return tk.Button(text=operation, bd=5, font=("Arial", 15), fg="red",
                    command=calculate)

def make_clear_button(operation):
    return tk.Button(text=operation, bd=5, font=("Arial", 15), fg="red",
                    command=clear)

def make_clear_one_button(operation):
    return tk.Button(text=operation, bd=5, font=("Arial", 15), fg="red",
                    command=clear_one)

def press_key(event):
    print(event.char)

screen = tk.Tk()
screen.geometry(f"240x350+300+200")
screen.title("Калькулятор")
screen.config(bg="#33ffe6")
screen.resizable(False, False)

screen.bind("<Key>", press_key)

make_digit_button("0").grid(row=5, column=0, sticky="wens",padx=5, pady=5)
make_digit_button("1").grid(row=2, column=0, sticky="wens",padx=5, pady=5)
make_digit_button("2").grid(row=2, column=1, sticky="wens",padx=5, pady=5)
make_digit_button("3").grid(row=2, column=2, sticky="wens",padx=5, pady=5)
make_digit_button("4").grid(row=3, column=0, sticky="wens",padx=5, pady=5)
make_digit_button("5").grid(row=3, column=1, sticky="wens",padx=5, pady=5)
make_digit_button("6").grid(row=3, column=2, sticky="wens",padx=5, pady=5)
make_digit_button("7").grid(row=4, column=0, sticky="wens",padx=5, pady=5)
make_digit_button("8").grid(row=4, column=1, sticky="wens",padx=5, pady=5)
make_digit_button("9").grid(row=4, column=2, sticky="wens",padx=5, pady=5)

calc = tk.Entry(screen, justify=tk.RIGHT, font=('Arial',20), width=15, validate="key")

calc.insert(0,"0")
calc.grid(row=0, column=0, columnspan=4, sticky="we", padx=5,pady=6)

make_operation_button("+").grid(row=3, column=3, sticky="wens",padx=5, pady=5)
make_operation_button("-").grid(row=4, column=3, sticky="wens",padx=5, pady=5)
make_operation_button("/").grid(row=1, column=3, sticky="wens",padx=5, pady=5)
make_operation_button("//").grid(row=1, column=1, sticky="wens",padx=5, pady=5)
make_operation_button("*").grid(row=2, column=3, sticky="wens",padx=5, pady=5)
make_operation_button("**").grid(row=1, column=2, sticky="wens",padx=5, pady=5)
make_calc_button("=").grid(row=5, column=3, sticky="wens",padx=5, pady=5)
make_clear_button("C").grid(row=1, column=0, sticky="wens",padx=5, pady=5)
make_clear_one_button("del").grid(row=5, column=1, sticky="wens",padx=5, pady=5)
make_operation_button(".").grid(row=5, column=2, sticky="wens",padx=5, pady=5)

screen.grid_columnconfigure(0, minsize=60)
screen.grid_columnconfigure(1, minsize=60)
screen.grid_columnconfigure(2, minsize=60)
screen.grid_columnconfigure(3, minsize=60)
screen.grid_columnconfigure(4, minsize=60)

screen.grid_rowconfigure(1, minsize=60)
screen.grid_rowconfigure(2, minsize=60)
screen.grid_rowconfigure(3, minsize=60)
screen.grid_rowconfigure(4, minsize=60)
screen.grid_rowconfigure(5, minsize=60)
screen.mainloop()