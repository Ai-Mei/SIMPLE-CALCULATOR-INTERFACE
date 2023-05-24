import tkinter as tk
from USERINTERFACE import UserInterface


root = tk.Tk()
root.configure(bg="#D9D7F1")
root.geometry("400x300")
root.title("My Calculator")

label = tk.Label(root, text="My Calculator", font=("Georgia", 16), bg="#D9D7F1", fg="#5E454B")
label.pack(padx=20, pady=10)

UserInterface(root)


root.mainloop()