import math
import time

class Node:
    def __init__(self, state, parent, depth, goal):
        self.state = state       #trạng thái hiện tại của Node (mảng chứa 2 phần tử là tọa độ x, y)
        self.parent = parent     #Node Sinh ra nodo này
        self.depth = depth       #Độ Sâu của node
        self.fcost(goal)       #Quảng đượng dự đoán để từ node đến đich

    def __eq__(self, state):#chông toán tử ==
        return self.state == state

    def fcost(self, goal):
        if self.parent != None:
            self.cost = self.parent.depth + math.sqrt((self.state[0] - goal[0]) ** 2 + (self.state[1] - goal[1]) ** 2)
        else:
            self.cost = math.sqrt((self.state[0] - goal[0]) ** 2 + (self.state[1] - goal[1]) ** 2)

def changeColor(lbtn, x, y, color):
    index = y + (x - 1) * 10 - 1
    lbtn[index].change_color(color)

def move(matrix, state, x, y):#Di chuyển, x, y là hướng di chuyển
    new_state = state[:]#tạo ra 1 state mới
    new_state[0] += y
    new_state[1] += x
    if matrix[new_state[0]][new_state[1]] == 0:#kiểm tra có bị chạm biên hoặc chạm vào cái tường
        return new_state
    else:
        return None

def CheckExplored(node, explored, frontier):#kiểm tra xem state dã tồn tại chưa
    for i in explored:
        if node == i:
            return 0  # tồn tại rồi
    for j in frontier:
        if node == j:
            return 0
    return 1#chưa tồn tại

def popFrontier(frontier, Tk, gif):
    index = 0
    for i in range(len(frontier)):
        if frontier[index].cost > frontier[i].cost:
            index = i
    changeColor(gif, frontier[index].state[0], frontier[index].state[1], "pink")
    Tk.update()
    #time.sleep(0.2)
    return frontier.pop(index)#trả về giá trị có cost nhỏ nhất

def Astar(Tk, gif, goal, start, matrix):
    operator = [[0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1]]
    frontier = []#những state đang chờ
    explored = []#nhưng state đang thực thi
    frontier.append(Node(start, None, 0, goal))#gán giá trị ban đầu cho frontier
    while len(frontier) > 0:#nếu frontier chưa none thì thực hiện
        node = popFrontier(frontier, Tk, gif)#lấy giá trị trong frontier
        explored.append(node)#add và tập đã thực thi
        if node == goal:
            moves = []  # tập chứa solution
            temp = node
            #print(temp.depth)
            temp = temp.parent
            while True:  # lấy solution
                moves.insert(0, temp.state)
                if temp.depth <= 1: break  # chạy đến node đầu tiên thì dừng vòng lập
                temp = temp.parent
            return moves
        for i in range(8):#action
            state_new = move(matrix, node.state, operator[i][0], operator[i][1])
            if state_new != None:#nếu khác node
                node_new = Node(state_new, node, node.depth + 1, goal)#tạo node mới
                if CheckExplored(node_new, frontier, explored):
                    frontier.append(node_new)#add và frontier
                    changeColor(gif, node_new.state[0], node_new.state[1], "aqua")
                    Tk.update()
                    time.sleep(0.2)
                    if node_new == goal: break
        changeColor(gif, node.state[0], node.state[1], "yellow")
        Tk.update()

    return None


import tkinter as tk
from tkinter import messagebox, ttk

win = tk.Tk()

matrix = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
lcb = []
start = [0, 0]
goal = [0, 0]


class Button:
    def Click(self):#click button
        if self.mode == 1:
            self.change_color('black')
            self.mode = 4
        elif self.mode == 2:
            self.change_color('red')
            self.mode = 4
        elif self.mode == 3:
            self.change_color('blue')
            self.mode = 4
        else:
            self.change_color('white')
            self.mode = 1
    def __init__(self, win, x, y):#hàm tạo
        self.btn = tk.Button(win, bg='white', width=4, height=2, command=self.Click)
        self.btn.grid(column=x, row=y)
        self.color = 'white'
        self.mode = 1# 1-matrix ;  2-goal   ;  3-start  ;  4-đã đc chọn

    def change_color(self, color):#hàm thay đổi màu sắc
        self.color = color
        self.btn.config(bg=color)

#tạo giao diện ma trận
lbtn = []
for i in range(10):
    for j in range(10):
        lbtn.append(Button(win, j, i))


def btn4_click():
    for i in range(100):
        if lbtn[i].color == 'black':
            x = int((i + 1) / 10) + 1
            y = (i + 1) % 10
            if y == 0:
                y += 10
                x -= 1
            matrix[x][y] = 1
        elif lbtn[i].color == 'blue':
            x = int((i + 1) / 10) + 1
            y = (i + 1) % 10
            if y == 0:
                y += 10
                x -= 1
            start[0] = x
            start[1] = y
        elif lbtn[i].color == 'red':
            x = int((i + 1) / 10) + 1
            y = (i + 1) % 10
            if y == 0:
                y += 10
                x -= 1
            goal[0] = x
            goal[1] = y
    if goal[0] != 0 and start[1] != 0:
        moves = Astar(win, lbtn, goal, start, matrix)
        changeColor(lbtn, goal[0], goal[1], 'red')
        changeColor(lbtn, start[0], start[1], 'blue')
        if moves != None:
            for i in range(len(moves)):
                changeColor(lbtn, moves[i][0], moves[i][1], "lawngreen")
            messagebox.showinfo(title='information', message='Hoàn thành')
        else:
            messagebox.showinfo(title='information', message='Không tìn được đường đi')
    else:
        messagebox.showinfo(title="information", message='Chưa điểm có bắt đầu hoặc kết thúc')
def btn1_click():
    for i in range(100):
        if lbtn[i].color == 'blue':
            lbtn[i].change_color('white')
        lbtn[i].mode = 3
def btn2_click():
    for i in range(100):
        if lbtn[i].color == 'red':
            lbtn[i].change_color('white')
        lbtn[i].mode = 2
def btn3_click():
    for i in range(100):
        if lbtn[i].mode != 4:
            lbtn[i].mode = 1
def Reset():
    global matrix
    global goal
    global start
    matrix = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
              [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
              [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
              [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
              [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
              [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
              [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
              [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
              [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
              [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    goal = [0, 0]
    start = [0, 0]
    for i in range(100):
        lbtn[i].mode = 1
        lbtn[i].change_color('white')

btn1 = ttk.Button(win, text='Start', command=btn1_click)
btn1.grid(column=11, row=3)
btn2 = ttk.Button(win, text='Goal', command=btn2_click)
btn2.grid(column=11, row=5)
btn3 = ttk.Button(win, text='Matrix', command=btn3_click)
btn3.grid(column=11, row=7)
btn4 = ttk.Button(win, text='Oke', command=btn4_click)
btn4.grid(column=11, row=9)
btn5 = ttk.Button(win, text='Reset', command=Reset)
btn5.grid(column=11, row=1)



win.mainloop()

