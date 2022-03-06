import tkinter as tk

root = tk.Tk()
root.resizable(False, False)
root.title("Tic Tac Toe")

tk.Label(root, text="Tic Tac Toe", font=('Ariel', 25)).pack()

current_chr = "X"

play_area = tk.Frame(root, width=300, height=300, bg='white')
XO_points = []
class XOPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.value = None
        self.button = tk.Button(play_area, text="", width=10, height=5, command=self.set)
        self.button.grid(row=x, column=y)

    def set(self):
        if not self.value:
            self.button.configure(text=current_chr, bg='snow', fg='black')
            self.value = current_chr

    def reset(self):
        self.button.configure(text="", bg='white')
        self.value = None
for x in range(3):
    for y in range(3):
        XO_points.append(XOPoint(x, y))
play_area.pack(pady=10, padx=10)

root.mainloop()
