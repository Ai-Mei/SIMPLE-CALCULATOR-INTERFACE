from USERINTERFACE import UserInterface
from NEWCALCULATOR import NewCalculator
from tkinter import messagebox
import tkinter as tk
new_cal = NewCalculator()

class NewUserInterface(UserInterface):

    def CreateWidgets(self):
        # Ask the user for inputs:
        label1 = tk.Label(self.root, text="Input the first number:", bg="#D9D7F1", fg="#354259")
        label1.pack()
        self.entry1 = tk.Entry(self.root)
        self.entry1.pack()

        label2 = tk.Label(self.root, text="Input the second number:", bg="#D9D7F1", fg="#354259")
        label2.pack()
        self.entry2 = tk.Entry(self.root)
        self.entry2.pack()

        # Enumeration and explanations per operation.
        message_text = "Please refer below for operations:\n\n+ for Addition\n\n- for substraction\n\n* for multiplication\n\n/ for division\n\n^ for number raise to n\n✩°｡ Note: 1st number is the \nbase and 2nd is the exponent\n"
        message_text_1 = "\n\n\n\n\nsqrt for squareroot\n✩°｡ Note: Please input only 1 number\n\nnthrt for raising the 1st\nnumber to power of\n2nd number\n\n! for factorial\n✩°｡ Note: Please input only 1 number\n\n% for percentage\n✩°｡ Note:\n1st number = number\n2nd number = percentage\n"
        message_frame = tk.Frame(bg="#D9D7F1")
        message_frame.pack()

        left_column = tk.Label(message_frame, text=message_text, justify=tk.LEFT, anchor='w', bg="#D9D7F1", fg="#205E61")
        left_column.grid(row=0, column=0, sticky="w")

        right_column = tk.Label(message_frame, text=message_text_1, justify=tk.LEFT, anchor='w', bg="#D9D7F1", fg="#205E61")
        right_column.grid(row=0, column=1, sticky= "w")

        # Ask user for operatuion
        label3 = tk.Label(self.root, text="Type the operation:", bg="#D9D7F1", fg="#AD8B73")
        label3.pack()
        self.entry3 = tk.Entry(self.root)
        self.entry3.pack()

        # Enter
        button = tk.Button(self.root, text="Process Inputs", bg="#FDEFEF", fg="#B980F0", command=self.execute)
        button.pack(pady=10)


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
        elif operation.lower() == "sqrt":
            result = new_cal.square_root(num_1)
        elif operation.lower() == "nthrt":
            result = new_cal.nth_root(num_1, num_2)
        elif operation == "!":
            result = new_cal.factorial(num_1)
        elif operation == "%":
            result = new_cal.percentage(num_1, num_2)


        else:
            messagebox.showerror("Invalid Input", "⚠️ Invalid operation. Please enter a valid operation (+, -, *, /, ^, sqrt, nthrt, !, %).")
            return

        loading_label = tk.Label(self.root, text="Loading", bg="#FDEFEF", fg="#FFACAC")
        loading_label.pack()
        self.animate_loading(loading_label, duration=5)
        messagebox.showinfo("Answer", f"Input 1: {num_1}\nInput 2: {num_2}\nOperation: {operation}\n{result}")
