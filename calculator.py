import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        # Entry widget to display input/output
        self.entry = tk.Entry(root, width=35, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Buttons
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), ("+", 4, 1), ("=", 4, 2), ("C", 4, 3)
        ]

        for (text, row, column) in buttons:
            tk.Button(root, text=text, width=10, command=lambda t=text: self.button_click(t)).grid(row=row, column=column, padx=5, pady=5)

    def button_click(self, value):
        current = self.entry.get()
        
        if value == "C":
            self.entry.delete(0, tk.END)
        elif value == "=":
            try:
                result = eval(current)
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(result))
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")
        else:
            self.entry.insert(tk.END, value)

def main():
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
