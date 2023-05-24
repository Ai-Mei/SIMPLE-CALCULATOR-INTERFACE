import tkinter as tk
from tkinter import messagebox
import time
from OPERATIONS import Operation
op = Operation()

class UserInterface:
    def __init__(self, root):
        self.root = root
        self.CreateWidgets()
    
    def CreateWidgets(self):
        # Ask the user for inputs:
        label1 = tk.Label(self.root, text="Input the first number:")
        label1.pack()
        self.entry1 = tk.Entry(self.root)
        self.entry1.pack()

        label2 = tk.Label(self.root, text="Input the second number:")
        label2.pack()
        self.entry2 = tk.Entry(self.root)
        self.entry2.pack()


        # Ask user for operatuion
        label3 = tk.Label(self.root, text="Type the operation:")
        label3.pack()
        self.entry3 = tk.Entry(self.root)
        self.entry3.pack()

        # Enter
        button = tk.Button(self.root, text="Process Inputs", command=self.execute)
        button.pack(pady=10)
 

    # Make a loading animation
    def animate_loading(self, loading_label, duration=5):
        start_time = time.time()
        part = 0
        while time.time() - start_time < duration:
            if part == 0:
                loading_label.config(text="Loading")
            elif part == 1:
                loading_label.config(text="⋆.ೃLoading࿔*:･*")
            elif part == 2:
                loading_label.config(text="°❀⋆.ೃLoading࿔*:･*:･⋆")
            elif part == 3:
                loading_label.config(text=".ೃ°❀⋆.ೃLoading࿔*:･*:･⋆.ೃ")
            elif part == 4:
                loading_label.config(text="⋆.ೃ°❀⋆.ೃLoading࿔*:･*:･⋆.ೃ࿔*:･")
            self.root.update()
            time.sleep(0.5)
            part = (part + 1) % 5


    def execute(self):
        num_1 = self.entry1.get()
        # Check if the input is a number.
        try:
            num_1 = float(num_1)
        except ValueError:
            messagebox.showerror("Invalid Input", "⚠️ Invalid value. Please enter a valid number.")
            return
        
        num_2 = self.entry2.get()
        # Check if the input is a number. 
        try:
            num_2 = float(num_2)
        except ValueError:
            messagebox.showerror("Invalid Input", "⚠️ Invalid value. Please enter a valid number.")
            return
        
        operation = self.entry3.get()
        operation = self.entry3.get()
        if operation == "+":
            result = op.Addition(num_1, num_2)
        elif operation == "-":
            result = op.Subtraction(num_1, num_2)
        elif operation == "*":
            result = op.Multiplication(num_1, num_2)
        elif operation == "/":
            result = op.Division(num_1, num_2)
        else:
            messagebox.showerror("Invalid Input", "Invalid operation. Please enter a valid operation (+, -, *, /).")
            return

        loading_label = tk.Label(self.root, text="Loading")
        loading_label.pack()
        self.animate_loading(loading_label, duration=5)
        messagebox.showinfo("Answer", f"Input 1: {num_1}\nInput 2: {num_2}\nOperation: {operation}")

       