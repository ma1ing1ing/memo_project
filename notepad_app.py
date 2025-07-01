import tkinter as tk

root = tk.Tk()
root.title("마린이의 메모장")
root.geometry("600x300")

text_area = tk.Text(root, font=("Helvectia", 12))

root.mainloop()