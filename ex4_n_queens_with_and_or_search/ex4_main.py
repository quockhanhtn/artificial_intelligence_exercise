#nguồn: code thầy phần class NQueensProblem:

# Solve N-queens problems using AND-OR search algorithm
'''
YOUR TASKS:
1. Read the given code to understand
2. Implement the and_or_graph_search() function
3. (Optinal) Add GUI, animation...
'''


import tkinter as tk
from PIL import ImageTk, Image
import time as t

class NQueensProblem:
    """The problem of placing N queens on an NxN board with none attacking each other.
    A state is represented as an N-element array, where a value of r in the c-th entry means there is a queen at column c,
    row r, and a value of -1 means that the c-th column has not been filled in yet. We fill in columns left to right.

    Sample code: iterative_deepening_search(NQueensProblem(8))
    Result: <Node (0, 4, 7, 5, 2, 6, 1, 3)>
    """

    def __init__(self, N):
        # self.initial = initial
        self.initial = tuple([-1] * no_of_queens) # mảng có giá trị là -1
        self.N = N #số con hậu

    def actions(self, state):
        """In the leftmost empty column, try all non-conflicting rows."""
        if state[-1] is not -1:#thêm đủ N con hậu rồi
            return []  # All columns filled; no successors
        else:
            col = state.index(-1)#lấy giá trị cột cầu thêm tiếp theo
            # return [(col, row) for row in range(self.N)
            return [row for row in range(self.N)#trả về một list các hành động
                    if not self.conflicted(state, row, col)]

    def goal_test(self, state):
        """Check if all columns filled, no conflicts."""
        if state[-1] is -1:#chưa là goal state
            return False
        return not any(self.conflicted(state, state[col], col)#trả về False nếu có ít nhất 1 cặp con hâu tấn công được nhau
                       for col in range(len(state)))

    def result(self, state, row):
        """Place the next queen at the given row."""
        col = state.index(-1)#lấy vị trí -1 tìm thấy đầu tiên
        new = list(state[:])
        new[col] = row#di chuyển con hậu lên hàng được truyền vào
        return tuple(new)#trả về state sau khi hành động

    def conflicted(self, state, row, col):
        """Would placing a queen at (row, col) conflict with anything?"""
        return any(self.conflict(row, col, state[c], c)#xét các con hậu có tấn công được nhau hay không
                   for c in range(col))#trả về true nếu có một con hậu cái thể tấn công nhau

    def conflict(self, row1, col1, row2, col2):
        """Would putting two queens in (row1, col1) and (row2, col2) conflict?"""
        return (row1 == row2 or  # same row
                col1 == col2 or  # same column
                row1 - col1 == row2 - col2 or  # same \ diagonal
                row1 + col1 == row2 + col2)  # same / diagonal

    def value(self, node):
        """Return (-) number of conflicting queens for a given node"""
        num_conflicts = 0
        for (r1, c1) in enumerate(node.state):
            for (r2, c2) in enumerate(node.state):
                if (r1, c1) != (r2, c2):
                    num_conflicts += self.conflict(r1, c1, r2, c2)

        return -num_conflicts


''' IMPLEMENT THE FOLLOWING FUNCTION '''

def and_or_graph_search(problem):
    """See [Figure 4.11] for the algorithm"""
    global timeN
    timeN = t.time()
    state = problem.initial
    path = []
    return (or_search(state, problem, path))

def or_search(state, problem, path):
    global clickStop
    global cStop
    if problem.goal_test(state):
        showGoal(state, problem.N, t.time())
        if (clickStop == True):
            cStop = True
        return []
    #if state in path: return None
    plans = []
    for action in problem.actions(state):
        #plan = and_search([problem.result(state, action)], problem, [state] + path)
        plan = and_search([problem.result(state, action)], problem, path)
        if plan is not None:
            plans.append([action, plan])
        if cStop == True:
            break
    if len(plans) > 0:
        return plans

    return None

def and_search(states, problem, path):
    plan = {}
    for s in states:
        plan[s] = or_search(s, problem, path)
        if plan[s] is None:
            return None
    return plan

def showGoal(solution, no, time):
    global win
    global listlb
    global img
    global lbtime
    global timeN
    global timeT
    global no_goal
    global lbno_goal

    no_goal += 1
    lbno_goal.config(text=no_goal)
    timeT += time - timeN

    lbtime.config(text=timeT)
    for i in range(len(solution)):
        for j in range(len(solution)):
            if (i + j) % 2 == 1:
                if j == solution[i]:
                    listlb[i*no + j].config(image=img[2])
                else:
                    listlb[i*no + j].config(image=img[0])
            else:
                if j == solution[i]:
                    listlb[i*no + j].config(image=img[3])
                else:
                    listlb[i*no + j].config(image=img[1])
    win.update()
    t.sleep(0.1)
    timeN = t.time()

def loadGui(no):
    global win
    global listlb
    str = no.__str__() + '-Queens'
    win.title(str)
    img = []

    img.append(ImageTk.PhotoImage(Image.open("Photo/1.PNG")))
    img.append(ImageTk.PhotoImage(Image.open("Photo/2.PNG")))
    img.append(ImageTk.PhotoImage(Image.open("Photo/3.PNG")))
    img.append(ImageTk.PhotoImage(Image.open("Photo/4.PNG")))

    for i in range(no):
        for j in range(no):
            if (i + j) % 2 == 1:
                listlb.append(tk.Label(win, image=img[0]))
                listlb[-1].grid(column=i, row=j)
            else:
                listlb.append(tk.Label(win, image=img[1]))
                listlb[-1].grid(column=i, row=j)
    win.update()

def btnStop_click():
    #t.sleep(60)
    global clickStop
    clickStop = True



if __name__ == '__main__':
    clickStop = False
    cStop = False

    listlb = []
    win = tk.Tk()
    img = []
    timeN = t.time()
    timeT = 0
    no_goal = 0
    img.append(ImageTk.PhotoImage(Image.open("Photo/1.PNG")))
    img.append(ImageTk.PhotoImage(Image.open("Photo/2.PNG")))
    img.append(ImageTk.PhotoImage(Image.open("Photo/3.PNG")))
    img.append(ImageTk.PhotoImage(Image.open("Photo/4.PNG")))


    no_of_queens =15;
    loadGui(no_of_queens)
    lbtext = tk.Label(win, text="   Time: ")
    lbtext.grid(column=no_of_queens + 1, row=1)
    lbtime = tk.Label(win, text="0", width=20)
    lbtime.grid(column=no_of_queens + 2, row=1)
    lbno_goal_text = tk.Label(win, text="  No_of_goal: ")
    lbno_goal_text.grid(column=no_of_queens + 1, row=3)
    lbno_goal = tk.Label(win, text="0", width=20)
    lbno_goal.grid(column=no_of_queens + 2, row=3)
    btnStop = tk.Button(win, command=btnStop_click, text="Break")
    btnStop.grid(column=no_of_queens + 2, row=5)
    win.update()
    problem1 = NQueensProblem(no_of_queens)

    result2 = and_or_graph_search(problem1)
    print(result2)


    win.mainloop()