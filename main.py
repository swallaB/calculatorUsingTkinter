import tkinter as tk
from file1 import MathFunctions


mf = MathFunctions()  # Creating instance of the MathFunctions class

class Calculator:

    def __init__(self, prim):
        prim.geometry('400x600')
        prim.title("Calculator")
        prim.configure(bg="black")
        prim.resizable(False, False)

        # Entry widget to enter the numbers for calculations
        top_frame = tk.Frame(prim, bg="black")
        top_frame.pack(padx=2)

        self.expression = ""
        self.value = tk.StringVar()

        self.entry = tk.Entry(top_frame, textvariable=self.value, font="Arial 20 bold", bg="black", fg="white", bd=5, relief="ridge")
        self.entry.grid(row=0, column=0, columnspan=20, sticky="we", ipady=50, padx=5, pady=5)

        button_frame = tk.Frame(prim, bg="black")
        button_frame.pack(padx=2)


        buttons = ["+", "-", "*", "/", "%", "1/x", "1", "2", "3", "sin", "x2", "4", "5", "6", "cos", "√x", "7", "8",
                   "9", "tan", "log", "(", "0", ")", "ln", "x!", "C", ".", "=", "|x|"]

        row = 1
        col = 0

        for button in buttons:
            if button.strip():  # Skip empty spaces
                action = lambda x=button: self.button_click(x)
                if row <= 5:
                    tk.Button(button_frame, text=button, width=9, height=4, font="Arial 9 bold", bg="#36454F", fg="#fff", command=action).grid(row=row, column=col,
                                                                                             padx=1, pady=1)
                else:
                    if col >= 1 and col <= 3:
                        tk.Button(button_frame, text=button, width=9, height=4, font="Arial 9 bold", bg="#ADD8E6", fg="#000", command=action).grid(row=row, column=col,
                                                                                         padx=1, pady=1)
                    else:
                        tk.Button(button_frame, text=button, width=9, height=4, font="Arial 9 bold", bg="#36454F", fg="#fff", command=action).grid(row=row, column=col,
                                                                  padx=1, pady=1)
            col += 1
            if col > 4:  # Move to the next row after 5 columns
                col = 0
                row += 1

    def button_click(self, val):
        # Safe function mapping
        safe_functions = {
            "+": mf.add,
            "-": mf.sub,
            "*": mf.mul,
            "/": mf.div,
            "%": mf.modulo,
            "1/x": mf.inverse,
            "x2": mf.sq,
            "√x": mf.sqrt,
            "log": mf.log,
            "ln": mf.ln,
            "sin": mf.sin,
            "cos": mf.cos,
            "tan": mf.tan,
            "x!": mf.factorial,
            "|x|": mf.absolute
        }

        if val == "=":
            try:
                # Safely evaluate the expression with the provided functions
                result = eval(self.expression, {"__builtins__": None}, safe_functions)
                self.value.set(result)
                self.expression = str(result)

            except Exception as e:
                self.value.set("error")
                self.expression = ""

        elif val == "C":
            self.expression = ""
            self.value.set("")
        else:
            # Handle operations
            self.expression += str(val)
            self.value.set(self.expression)
            print(self.expression)


# Main Tkinter window
root = tk.Tk()
calc = Calculator(root)
root.mainloop()
