
# Solve N-queens problem using Min-conflicts algorithm
'''
YOUR TASKS:
1. Read to understand the following code 
2. Give comments on the min_conflicts() function to show your comprehensive understanding of the code
3. (Optional) Add GUI, animation...
'''

import random

#%% Utilities:
def argmin_random_tie(seq, key=lambda x: x):
    """Return a minimum element of seq; break ties at random."""
    items = list(seq)
    random.shuffle(items) #Randomly shuffle a copy of seq.
    return min(items, key=key)

class UniversalDict:
    """A universal dict maps any key to the same value. We use it here
    as the domains dict for CSPs in which all variables have the same domain.
    >>> d = UniversalDict(42)
    >>> d['life']
    42
    """      
    def __init__(self, value): self.value = value

    def __getitem__(self, key): return self.value

    def __repr__(self): return '{{Any: {0!r}}}'.format(self.value)


#%% CSP
class CSP():
    """This class describes finite-domain Constraint Satisfaction Problems.
    A CSP is specified by the following inputs:
        variables   A list of variables; each is atomic (e.g. int or string).
        domains     A dict of {var:[possible_value, ...]} entries.
        neighbors   A dict of {var:[var,...]} that for each variable lists
                    the other variables that participate in constraints.
        constraints A function f(A, a, B, b) that returns true if neighbors
                    A, B satisfy the constraint when they have values A=a, B=b
    """

    def __init__(self, variables, domains, neighbors, constraints):
        """Construct a CSP problem. If variables is empty, it becomes domains.keys()."""
        #super().__init__(())
        variables = variables or list(domains.keys())
        self.variables = variables
        self.domains = domains
        self.neighbors = neighbors
        self.constraints = constraints
        self.curr_domains = None
        self.nassigns = 0

    def assign(self, var, val, assignment):
        """Add {var: val} to assignment; Discard the old value if any."""
        assignment[var] = val
        self.nassigns += 1

    def unassign(self, var, assignment):
        """Remove {var: val} from assignment.
        DO NOT call this if you are changing a variable to a new value;
        just call assign for that."""
        if var in assignment:
            del assignment[var]

    def nconflicts(self, var, val, assignment):
        """Return the number of conflicts var=val has with other variables."""

        # Subclasses may implement this more efficiently
        def conflict(var2):
            return var2 in assignment and not self.constraints(var, val, var2, assignment[var2])

        return count(conflict(v) for v in self.neighbors[var])

    # This is for min_conflicts search  
    def conflicted_vars(self, current):
        """Return a list of variables in current assignment that are in conflict"""
        return [var for var in self.variables
                if self.nconflicts(var, current[var], current) > 0]


#%% N-queens problem
def queen_constraint(A, a, B, b):
    """Constraint is satisfied (true) if A, B are really the same variable,
    or if they are not in the same row, down diagonal, or up diagonal."""
    return A == B or (a != b and A + a != B + b and A - a != B - b)

class NQueensCSP(CSP):
    """
    Make a CSP for the nQueens problem for search with min_conflicts.
    Suitable for large n, it uses only data structures of size O(n).
    Think of placing queens one per column, from left to right.
    That means position (x, y) represents (var, val) in the CSP.
    The main structures are three arrays to count queens that could conflict:
        rows[i]      Number of queens in the ith row (i.e. val == i)
        downs[i]     Number of queens in the \ diagonal
                     such that their (x, y) coordinates sum to i
        ups[i]       Number of queens in the / diagonal
                     such that their (x, y) coordinates have x-y+n-1 = i
    """

    def __init__(self, n):
        """Initialize data structures for n Queens."""
        CSP.__init__(self, list(range(n)), UniversalDict(list(range(n))),
                     UniversalDict(list(range(n))), queen_constraint)

        self.rows = [0] * n
        self.ups = [0] * (2 * n - 1)
        self.downs = [0] * (2 * n - 1)

    def nconflicts(self, var, val, assignment):
        """The number of conflicts, as recorded with each assignment.
        Count conflicts in row and in up, down diagonals. If there
        is a queen there, it can't conflict with itself, so subtract 3."""
        n = len(self.variables)
        c = self.rows[val] + self.downs[var + val] + self.ups[var - val + n - 1]
        if assignment.get(var, None) == val:
            c -= 3
        return c

    def assign(self, var, val, assignment):
        """Assign var, and keep track of conflicts."""
        old_val = assignment.get(var, None)
        if val != old_val:
            if old_val is not None:  # Remove old val if there was one
                self.record_conflict(assignment, var, old_val, -1)
            self.record_conflict(assignment, var, val, +1)
            CSP.assign(self, var, val, assignment)

    def unassign(self, var, assignment):
        """Remove var from assignment (if it is there) and track conflicts."""
        if var in assignment:
            self.record_conflict(assignment, var, assignment[var], -1)
        CSP.unassign(self, var, assignment)

    def record_conflict(self, assignment, var, val, delta):
        """Record conflicts caused by addition or deletion of a Queen."""
        n = len(self.variables)
        self.rows[val] += delta
        self.downs[var + val] += delta
        self.ups[var - val + n - 1] += delta


#%% Min-conflicts for CSPs
''' READ AND COMMENT to show your comprehensive understanding of the following function '''
def min_conflicts(csp, max_steps=100000):
    """See Figure 6.8 for the algorithm"""
    csp.current = current = {}
    for var in csp.variables:
        value = min_conflicts_value(csp, var, current)
        csp.assign(var, value, current)
    
    for i in range(max_steps):
        conflicted = csp.conflicted_vars(current)
        if not conflicted:
            return current
        var = random.choice(conflicted)
        value = min_conflicts_value(csp, var, current)
        csp.assign(var, value, current)
    return None

def min_conflicts_value(csp, var, current):
    """Return the value that will give var the least number of conflicts.
    If there is a tie, choose at random."""
    return argmin_random_tie(csp.domains[var], key=lambda val: csp.nconflicts(var, val, current))


from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

def resize_img(img, new_width) :
    '''
    Resize an image and maintain its aspect ratio
    Input : img, new_width
    Output: new image has width = new_width
    '''
    wpercent = (new_width / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((int(new_width), hsize), Image.ANTIALIAS)

    return img

#%% GUI
class Ui_NQueens:
    '''GUI for NQueens'''
    def __init__(self, default_no_of_queens):
        self.queen_img = 0
        self.no_of_queens = default_no_of_queens

        self.window = Tk()
        self.window.title("Solve N Queens on chessboarde with Min conflicts")

        # chia window thành 2 khung left_frame và right_frame
        # tham khảo code của thành viên CommonSense: 
        # link https://stackoverflow.com/questions/46522200/how-to-make-two-split-up-screen-canvas-inside-the-python-tkinter-window
        self.left_frame = Frame(self.window, borderwidth=0, relief="solid")
        self.right_frame = Frame(self.window, borderwidth=0, relief="solid")
        self.left_frame.pack(side="left", expand=True, fill="both")
        self.right_frame.pack(side="right", expand=True, fill="both")

        # Tạo canvas hiển thị bàn cờ
        self.canvas = Canvas(master=self.left_frame, width=980, height=980, background="black")
        self.canvas.pack()

        # Tạo ra label hiện 'No of queens:'
        self.label_no_queens = Label(master=self.right_frame, text='No of queens:')
        self.label_no_queens.pack()

        # Tạo ra textbox số lượng quân hậu
        self.entry_no_queens = Entry(master=self.right_frame, justify='center', width = 10)
        self.entry_no_queens.insert(0, str(self.no_of_queens))
        self.entry_no_queens.bind("<Return>", lambda x: self.set_no_queens(self.entry_no_queens.get()))
        self.entry_no_queens.pack()

        # Tạo ra button 'And or search'
        self.button_solve = Button(master=self.right_frame, text='Min conflicts', command=lambda:self.set_no_queens(self.entry_no_queens.get()))
        self.button_solve.pack()

        self.update_canvas()
        self.set_no_queens(self.entry_no_queens.get())

    def update_canvas(self, list_queens = None, black_cell_color = '#949698', while_cell_color = '#fafafa', margin = 5):
        ''' Update canvas by "list_queens" (if had) '''

        self.canvas.update()
        # lấy kích thước của canvas
        cell_width = (self.canvas.winfo_width() - margin * 2) / self.no_of_queens
        cell_height = (self.canvas.winfo_height() - margin * 2) / self.no_of_queens

        # chọn kích thước ô cờ
        cell_size = cell_width if (cell_height > cell_width) else cell_height

        x, y = margin, margin
        # vẽ các ô trên bàn cờ
        for i in range(self.no_of_queens):
            for j in range(self.no_of_queens) :
                x1, y1 = x, y
                x2, y2 = x1 + cell_size, y +  cell_size

                # Vẽ hình chữ nhật
                # tham khảo http://zetcode.com/tkinter/drawing/
                if ((i + j) % 2 == 0) : # vẽ ô cờ trắng
                    self.canvas.create_rectangle(x1, y1, x2, y2, outline="", fill=while_cell_color)
                else :                  # vẽ ô cờ đen
                    self.canvas.create_rectangle(x1, y1, x2, y2, outline="", fill=black_cell_color)

                x = x + cell_size
            x = margin
            y = y + cell_size
    
        # Nguồn ảnh : https://www.pngbarn.com/png-image-lfeqi?__cf_chl_captcha_tk__=0ecb57416ccd4ffd0fd461e96826ebbe5443f243-1589871646-0-Ab5eix4dmDECKHvlpaA4JPSzpJveXnygc200nOx-5rzqp8EV5OfAiJnP2-rKbgScov5GqAQHG2doEqn3MJHVvVwAyz3A1zmqCldtTYs9pCHKfDJS9Gik4jQvnbdEz6rqPtG042LfSzO7ypjDuJi_2WCNYaom5-OfyggxRxdiEcVekIwTgtKftTLRvOZw7DTE3XhikKzo1Ak1J5rUxh_DdgugI8N66TBl6NpqRCHDEkO8qNM3tn2j_dPeWLGIRdm3bvDPtW3LFnFJ70XjOHjUFl6z4EbfIeiHGD6ArUMMh5kpJLljlTSUm75kApv3AHr-dD4DYY5Pd1lj7BMDF0MVsuaVLyzp769PCV3vqhdSV4qjrpzievPYGqIrJ-Jh5-g9-5E4mYzz9NawtwJVz-7G7etD3Q2ZByoxOe6YrAYyWwqUVE8SZa8sG0Z2rVtlIvDjJkVGXP4YlMKX8vk_EpdTTOTDbOLimcS5EY8Piq7GN0YBmRIa_HBxapiJwstlrgppf9YJLc7MPIk0s8PRelHGTaE
        raw_queen_img = Image.open('img\queen.png')
        self.queen_img = ImageTk.PhotoImage(resize_img(raw_queen_img, cell_size))

        # hiển thị các quân hậu theo list_queens
        if (list_queens != None):
            for j in range(self.no_of_queens) :
                if (list_queens[j] != -1):
                    x = margin + cell_size * j
                    y = margin + cell_size * list_queens[j]
                    self.canvas.create_image(x, y, anchor = NW, image=self.queen_img)

    def set_no_queens(self, input_value):
        '''Set no of queens by input textbox'''
        try:
            self.no_of_queens = int(input_value)
            if(self.no_of_queens < 4) :
                messagebox.showinfo("Lỗi","Bạn phải nhập số nguyên dương lớn hơn 3")
                return
        except ValueError:
            messagebox.showinfo("Lỗi","Bạn phải nhập số nguyên dương lớn hơn 3")
            return

        self.update_canvas()

        queens_problem = NQueensCSP(n=self.no_of_queens)
        min_conflicts(queens_problem, max_steps=100000); 
        result = queens_problem.current

        if (result) :
            self.update_canvas(queens_problem.current)
            messagebox.showinfo("Hoàn thành","Đã sắp xếp xong các quân hậu")
        else :
            messagebox.showinfo("Lỗi","Không sắp xếp được")

#%% Main program
def main():
    ui = Ui_NQueens(default_no_of_queens = 50)
    ui.window.mainloop()

if __name__ == '__main__':
    main()

