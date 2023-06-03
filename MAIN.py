import tkinter as tk
from NEWUSERINTERFACE import NewUserInterface


root = tk.Tk()
root.configure(bg="#D9D7F1")
root.geometry("400x800")
root.title("My Calculator")

label = tk.Label(root, text="  ╱|、\n    (˚ˎ 。7  \n            |、˜〵          \n       じしˍ,)ノ\nMy Calculator", font=("Georgia", 16), bg="#D9D7F1", fg="#5E454B")
label.pack(padx=20)


NewUserInterface(root)


root.mainloop()

