import tkinter as tk
root = tk.Tk()
class UserInterface:
    def execute():
        num_1 = entry1.get()

#Ask the user for input
label1 = tk.Label(root, text="Input the first number:")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()


root.mainloop()
