from USERINTERFACE import UserInterface
from NEWCALCULATOR import NewCalculator
from tkinter import messagebox
import tkinter as tk
new_cal = NewCalculator()

class NewUserInterface(UserInterface):
    def execute(self):
        num_1 = self.entry1.get()
        # Check if the input is a number.
        try:
            num_1 = float(num_1)
        except ValueError:
            messagebox.showerror("Invalid Input", "⚠️ Invalid value. Please enter a valid number.")
            return
        
        num_2 = self.entry2.get()
        if num_2.strip() != "":
            try:
                num_2 = float(num_2)
            except ValueError:
                # Input is not a valid number
                messagebox.showerror("Invalid Input", "⚠️ Invalid value. Please enter a valid number.")
                return
        else:
            if num_2.strip() == "":
                pass
        
        operation = self.entry3.get()
        operation = self.entry3.get()
        if operation == "+":
            result = new_cal.addition(num_1, num_2)
        elif operation == "-":
            result = new_cal.subtraction(num_1, num_2)
        elif operation == "*":
            result = new_cal.multiplication(num_1, num_2)
        elif operation == "/":
            result = new_cal.division(num_1, num_2)
        # Added the new methods.
        elif operation == "^":
            result = new_cal.raise_to_nth_power(num_1, num_2)
        else:
            messagebox.showerror("Invalid Input", "⚠️ Invalid operation. Please enter a valid operation (+, -, *, /).")
            return

        loading_label = tk.Label(self.root, text="Loading", bg="#FDEFEF", fg="#FFACAC")
        loading_label.pack()
        self.animate_loading(loading_label, duration=5)
        messagebox.showinfo("Answer", f"Input 1: {num_1}\nInput 2: {num_2}\nOperation: {operation}\n{result}")
