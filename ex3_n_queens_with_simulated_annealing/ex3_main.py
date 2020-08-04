from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from algorithm import *

no_of_queens = 0
queen_img = 0

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

def update_canvas(canvas, no_of_queens, list_queens = None, black_cell_color = '#949698', while_cell_color = '#fafafa', margin = 5):
    '''
    Cập nhật "canvas" theo "no_of_queens" và "list_queens"
    '''
    global queen_img 
    canvas.update()

    # lấy kích thước của canvas
    cell_width = (canvas.winfo_width() - margin * 2) / no_of_queens
    cell_height = (canvas.winfo_height() - margin * 2) / no_of_queens

    # 
    cell_size = cell_width if (cell_height > cell_width) else cell_height

    x, y = margin, margin
    # vẽ các ô trên bàn cờ
    for i in range(no_of_queens):
        for j in range(no_of_queens) :
            x1, y1 = x, y
            x2, y2 = x1 + cell_size, y +  cell_size

            # Vẽ hình chữ nhật
            # tham khảo http://zetcode.com/tkinter/drawing/
            if ((i + j) % 2 == 0) :
                # vẽ ô cờ trắng
                canvas.create_rectangle(x1, y1, x2, y2, outline="", fill=while_cell_color)
            else :
                # vẽ ô cờ đen
                canvas.create_rectangle(x1, y1, x2, y2, outline="", fill=black_cell_color)

            x = x + cell_size
        x = margin
        y = y + cell_size
    
    # Nguồn ảnh : https://www.pngbarn.com/png-image-lfeqi?__cf_chl_captcha_tk__=0ecb57416ccd4ffd0fd461e96826ebbe5443f243-1589871646-0-Ab5eix4dmDECKHvlpaA4JPSzpJveXnygc200nOx-5rzqp8EV5OfAiJnP2-rKbgScov5GqAQHG2doEqn3MJHVvVwAyz3A1zmqCldtTYs9pCHKfDJS9Gik4jQvnbdEz6rqPtG042LfSzO7ypjDuJi_2WCNYaom5-OfyggxRxdiEcVekIwTgtKftTLRvOZw7DTE3XhikKzo1Ak1J5rUxh_DdgugI8N66TBl6NpqRCHDEkO8qNM3tn2j_dPeWLGIRdm3bvDPtW3LFnFJ70XjOHjUFl6z4EbfIeiHGD6ArUMMh5kpJLljlTSUm75kApv3AHr-dD4DYY5Pd1lj7BMDF0MVsuaVLyzp769PCV3vqhdSV4qjrpzievPYGqIrJ-Jh5-g9-5E4mYzz9NawtwJVz-7G7etD3Q2ZByoxOe6YrAYyWwqUVE8SZa8sG0Z2rVtlIvDjJkVGXP4YlMKX8vk_EpdTTOTDbOLimcS5EY8Piq7GN0YBmRIa_HBxapiJwstlrgppf9YJLc7MPIk0s8PRelHGTaE
    raw_queen_img = Image.open('img\queen.png')
    queen_img = ImageTk.PhotoImage(resize_img(raw_queen_img, cell_size))

    # hiển thị các quân hậu theo list_queens
    if (list_queens != None):
        for j in range(no_of_queens) :
            y = margin + cell_size * list_queens[j]
            x = margin + cell_size * j
            canvas.create_image(x, y, anchor = NW, image=queen_img)
    pass

def set_no_queens(input_value):
    global canvas, no_of_queens
    try:
        no_of_queens = int(input_value)
        if(no_of_queens < 8) :
            messagebox.showinfo("Lỗi","Bạn phải nhập số nguyên dương lớn hơn 7")
            return
    except ValueError:
        messagebox.showinfo("Lỗi","Bạn phải nhập số nguyên dương lớn hơn 7")
        return

    update_canvas(canvas, no_of_queens)
    solution = simulated_annealing(no_of_queens)
    update_canvas(canvas, no_of_queens, solution.list_queens)
    messagebox.showinfo("Hoàn thành","Đã sắp xếp xong các quân hậu")
    pass

window = Tk()
window.title("Queen")

# chia window thành 2 khung left_frame và right_frame
# tham khảo code của thành viên CommonSense: 
# link https://stackoverflow.com/questions/46522200/how-to-make-two-split-up-screen-canvas-inside-the-python-tkinter-window
left_frame = Frame(window, borderwidth=0, relief="solid")
right_frame = Frame(window, borderwidth=0, relief="solid")
left_frame.pack(side="left", expand=True, fill="both")
right_frame.pack(side="right", expand=True, fill="both")

canvas = Canvas(master = left_frame, width=800, height=800, background="black")
canvas.pack()


label_no_queens = Label(master=right_frame, text='No of queens:')
label_no_queens.pack()

# Tạo ra textbox số lượng quân hậu
entry_no_queens = Entry(master=right_frame)
entry_no_queens.insert(0, "15")
entry_no_queens.bind("<Return>", lambda x: set_no_queens(entry_no_queens.get()))
entry_no_queens.pack()

button_solve = Button(master=right_frame, text='Simulated annealing', command=lambda:set_no_queens(entry_no_queens.get()))
button_solve.pack()

set_no_queens(entry_no_queens.get())

window.mainloop()