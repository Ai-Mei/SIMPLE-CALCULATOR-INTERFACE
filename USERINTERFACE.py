import tkinter as tk
from tkinter import messagebox


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
 
    def execute(self):
        num_1 = self.entry1.get()
        num_2 = self.entry2.get()
        operation = self.entry3.get()
        messagebox.showinfo("Answer", f"Input 1: {num_1}\nInput 2: {num_2}\nOperation: {operation}")

       