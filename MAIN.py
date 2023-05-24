import tkinter as tk
from USERINTERFACE import UserInterface
ui = UserInterface

root = tk.Tk()
root.geometry("400x300")
root.title("My Calculator")

label = tk.Label(root, text="My Calculator", font=("Georgia", 16))
label.pack(padx=20, pady=10)

ui.UserInput()


root.mainloop()