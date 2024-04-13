from tkinter import *
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")

        self.equation = StringVar()

        self.display = Entry(root, textvariable=self.equation, font=('Arial', 20))
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        self.buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('/', 4, 2), ('%', 4, 3)
        ]

        self.create_buttons()

    def create_buttons(self):
        for (text, row, col) in self.buttons:
            button = Button(self.root, text=text, font=('Arial', 16), padx=20, pady=20,
                            command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, sticky="nsew")
        

        Button(self.root, text='C', font=('Arial', 16), padx=20, pady=20, command=self.clear).grid(row=5, column=0, sticky="nsew")
        Button(self.root, text='=', font=('Arial', 16), padx=20, pady=20, command=self.calculate).grid(row=5, column=1, columnspan=2, sticky="nsew")
        Button(self.root, text='←', font=('Arial', 16), padx=20, pady=20, command=self.delete_last).grid(row=5, column=3, sticky="nsew")
        Button(self.root, text='sin', font=('Arial', 16), padx=20, pady=20, command=lambda: self.trig_function('sin')).grid(row=6, column=0, sticky="nsew")
        Button(self.root, text='cos', font=('Arial', 16), padx=20, pady=20, command=lambda: self.trig_function('cos')).grid(row=6, column=1, sticky="nsew")
        Button(self.root, text='tan', font=('Arial', 16), padx=20, pady=20, command=lambda: self.trig_function('tan')).grid(row=6, column=2, sticky="nsew")
        Button(self.root, text='√', font=('Arial', 16), padx=20, pady=20, command=self.square_root).grid(row=6, column=3, sticky="nsew")

    def on_button_click(self, char):
        current_equation = self.equation.get()
        new_equation = current_equation + str(char)
        self.equation.set(new_equation)

    def clear(self):
        self.equation.set("")

    def delete_last(self):
        current_equation = self.equation.get()
        new_equation = current_equation[:-1]
        self.equation.set(new_equation)

    def calculate(self):
        try:
            expression = self.equation.get()
            result = eval(expression)
            self.equation.set(result)
        except Exception as e:
            self.equation.set("Error")

    def trig_function(self, func):
        try:
            value = float(self.equation.get())
            if func == 'sin':
                result = math.sin(math.radians(value))
            elif func == 'cos':
                result = math.cos(math.radians(value))
            elif func == 'tan':
                result = math.tan(math.radians(value))
            self.equation.set(result)
        except Exception as e:
            self.equation.set("Error")

    def square_root(self):
        try:
            value = float(self.equation.get())
            if value >= 0:
                result = math.sqrt(value)
                self.equation.set(result)
            else:
                self.equation.set("Error")
        except Exception as e:
            self.equation.set("Error")


root = Tk()
app = Calculator(root)
root.mainloop()
