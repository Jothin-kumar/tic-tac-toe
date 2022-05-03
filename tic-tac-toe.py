import tkinter as tk

root = tk.Tk()
root.resizable(False, False)
root.title("Tic Tac Toe")

tk.Label(root, text="Tic Tac Toe", font=('Ariel', 25)).pack()
status_label = tk.Label(root, text="X's turn", font=('Ariel', 15), bg='green', fg='snow')
status_label.pack(fill=tk.X)
def play_again():
    global current_chr
    current_chr = 'X'
    for point in XO_points:
        point.button.configure(state=tk.NORMAL)
        point.reset()
    status_label.configure(text="X's turn")
    play_again_button.pack_forget()
play_again_button = tk.Button(root, text='Play again', font=('Ariel', 15), command=play_again)

current_chr = "X"

play_area = tk.Frame(root, width=300, height=300, bg='white')
XO_points = []
X_points = []
O_points = []
class XOPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.value = None
        self.button = tk.Button(play_area, text="", width=10, height=5, command=self.set)
        self.button.grid(row=x, column=y)

    def set(self):
        global current_chr
        if not self.value:
            self.button.configure(text=current_chr, bg='snow', fg='black')
            self.value = current_chr
            if current_chr == "X":
                X_points.append(self)
                current_chr = "O"
                status_label.configure(text="O's turn")
            elif current_chr == "O":
                O_points.append(self)
                current_chr = "X"
                status_label.configure(text="X's turn")
        check_win()

    def reset(self):
        self.button.configure(text="", bg='lightgray')
        if self.value == "X":
            X_points.remove(self)
        elif self.value == "O":
            O_points.remove(self)
        self.value = None
for x in range(1, 4):
    for y in range(1, 4):
        XO_points.append(XOPoint(x, y))
class WinningPossibility:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
    def check(self, for_chr):
        self.p1_satisfied = False
        self.p2_satisfied = False
        self.p3_satisfied = False
        if for_chr == 'X':
            for point in X_points:
                if point.x == self.x1 and point.y == self.y1:
                    self.p1_satisfied = True
                elif point.x == self.x2 and point.y == self.y2:
                    self.p2_satisfied = True
                elif point.x == self.x3 and point.y == self.y3:
                    self.p3_satisfied = True
        elif for_chr == 'O':
            for point in O_points:
                if point.x == self.x1 and point.y == self.y1:
                    self.p1_satisfied = True
                elif point.x == self.x2 and point.y == self.y2:
                    self.p2_satisfied = True
                elif point.x == self.x3 and point.y == self.y3:
                    self.p3_satisfied = True
        return all([self.p1_satisfied, self.p2_satisfied, self.p3_satisfied])
winning_possibilities = [
    WinningPossibility(1, 1, 1, 2, 1, 3),
    WinningPossibility(2, 1, 2, 2, 2, 3),
    WinningPossibility(3, 1, 3, 2, 3, 3),
    WinningPossibility(1, 1, 2, 1, 3, 1),
    WinningPossibility(1, 2, 2, 2, 3, 2),
    WinningPossibility(1, 3, 2, 3, 3, 3),
    WinningPossibility(1, 1, 2, 2, 3, 3),
    WinningPossibility(3, 1, 2, 2, 1, 3)
]
def disable_game():
    for point in XO_points:
        point.button.configure(state=tk.DISABLED)
    play_again_button.pack()
def check_win():
    for possibility in winning_possibilities:
        if possibility.check('X'):
            status_label.configure(text="X won!")
            disable_game()
            return
        elif possibility.check('O'):
            status_label.configure(text="O won!")
            disable_game()
            return
    if len(X_points) + len(O_points) == 9:
        status_label.configure(text="Draw!")
        disable_game()
play_area.pack(pady=10, padx=10)


def auto_play():

    # If winning is possible in the next move
    for winning_possibility in winning_possibilities:
        winning_possibility.check('O')
        if winning_possibility.p1_satisfied and winning_possibility.p2_satisfied:
            for point in XO_points:
                if point.x == winning_possibility.x3 and point.y == winning_possibility.y3 and point not in X_points + O_points:
                    point.set()
                    return
        elif winning_possibility.p2_satisfied and winning_possibility.p3_satisfied:
            for point in XO_points:
                if point.x == winning_possibility.x1 and point.y == winning_possibility.y1 and point not in X_points + O_points:
                    point.set()
                    return
        elif winning_possibility.p3_satisfied and winning_possibility.p1_satisfied:
            for point in XO_points:
                if point.x == winning_possibility.x2 and point.y == winning_possibility.y2 and point not in X_points + O_points:
                    point.set()
                    return

    # If the opponent can win in the next move
    for winning_possibility in winning_possibilities:
        winning_possibility.check('X')
        if winning_possibility.p1_satisfied and winning_possibility.p2_satisfied:
            for point in XO_points:
                if point.x == winning_possibility.x3 and point.y == winning_possibility.y3 and point not in X_points + O_points:
                    point.set()
                    return
        elif winning_possibility.p2_satisfied and winning_possibility.p3_satisfied:
            for point in XO_points:
                if point.x == winning_possibility.x1 and point.y == winning_possibility.y1 and point not in X_points + O_points:
                    point.set()
                    return
        elif winning_possibility.p3_satisfied and winning_possibility.p1_satisfied:
            for point in XO_points:
                if point.x == winning_possibility.x2 and point.y == winning_possibility.y2 and point not in X_points + O_points:
                    point.set()
                    return

    # If the center is free...
    center_occupied = False
    for point in X_points + O_points:
        if point.x == 2 and point.y == 2:
            center_occupied = True
            break
    if not center_occupied:
        for point in XO_points:
            if point.x == 2 and point.y == 2:
                point.set()
                return

    # Occupy corner or middle based on what opponent occupies
    corner_points = [(1, 1), (1, 3), (3, 1), (3, 3)]
    middle_points = [(1, 2), (2, 1), (2, 3), (3, 2)]
    num_of_corner_points_occupied_by_X = 0
    for point in X_points:
        if (point.x, point.y) in corner_points:
            num_of_corner_points_occupied_by_X += 1
    if num_of_corner_points_occupied_by_X >= 2:
        for point in XO_points:
            if (point.x, point.y) in middle_points and point not in X_points + O_points:
                point.set()
                return
    elif num_of_corner_points_occupied_by_X < 2:
        for point in XO_points:
            if (point.x, point.y) in corner_points and point not in X_points + O_points:
                point.set()
                return

root.mainloop()
