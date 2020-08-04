from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget, QMessageBox
from PyQt5.Qt import Qt
from PyQt5.QtCore import *
from .cons import *
from .Functions import *
from .search_algorithm import *

class QLinkLabel(QtWidgets.QLabel):
    """"""
    def __init__(self, parent=None, link=''):
        QtWidgets.QLabel.__init__(self, parent)
        self.setStyleSheet('color: blue')
        self.link = link

    def mousePressEvent(self, event):
        Functions.open_web(self.link)

class UIMainWindow(object):
    def __init__(self, puzzle_stage):
        self.puzzle_stage = puzzle_stage
        self.main_window = QtWidgets.QMainWindow()
        self.main_window.setObjectName("main_window")
        self.main_window.setFixedSize(1557, 564)
        self.main_window.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.setup_ui()

    def center(self):
        '''
        Center self.main_window on screen
        ref : https://gist.github.com/saleph/163d73e0933044d0e2c4
        '''
        qr = self.main_window.frameGeometry()
        # center point of screen
        cp = QDesktopWidget().availableGeometry().center()
        # move rectangle's center point to screen's center point
        qr.moveCenter(cp)
        # top left of rectangle becomes top left of window centering it
        self.main_window.move(qr.topLeft())

    def setup_ui(self):
        self.centralwidget = QtWidgets.QWidget(self.main_window)
        self.centralwidget.setMaximumSize(QtCore.QSize(1557, 564))
        self.centralwidget.setObjectName("centralwidget")
        self.grp_puzzle = QtWidgets.QGroupBox(self.centralwidget)
        self.grp_puzzle.setGeometry(QtCore.QRect(5, 5, 1028, 554))
        self.grp_puzzle.setTitle("")
        self.grp_puzzle.setFlat(False)
        self.grp_puzzle.setCheckable(False)
        self.grp_puzzle.setObjectName("grp_puzzle")
        self.label_img_0 = QtWidgets.QLabel(self.grp_puzzle)
        self.label_img_0.setGeometry(QtCore.QRect(5, 5, 336, 178))
        self.label_img_0.setStyleSheet("image: " + cons.img_url[0])
        self.label_img_0.setText("")
        self.label_img_0.setObjectName("label_img_0")
        self.label_img_1 = QtWidgets.QLabel(self.grp_puzzle)
        self.label_img_1.setGeometry(QtCore.QRect(346, 5, 336, 178))
        self.label_img_1.setStyleSheet("image: " + cons.img_url[1])
        self.label_img_1.setText("")
        self.label_img_1.setObjectName("label_img_1")
        self.label_img_2 = QtWidgets.QLabel(self.grp_puzzle)
        self.label_img_2.setGeometry(QtCore.QRect(687, 5, 336, 178))
        self.label_img_2.setStyleSheet("image: " + cons.img_url[2])
        self.label_img_2.setText("")
        self.label_img_2.setObjectName("label_img_2")
        self.label_img_3 = QtWidgets.QLabel(self.grp_puzzle)
        self.label_img_3.setGeometry(QtCore.QRect(5, 188, 336, 178))
        self.label_img_3.setStyleSheet("image: " + cons.img_url[3])
        self.label_img_3.setText("")
        self.label_img_3.setObjectName("label_img_3")
        self.label_img_4 = QtWidgets.QLabel(self.grp_puzzle)
        self.label_img_4.setGeometry(QtCore.QRect(346, 188, 336, 178))
        self.label_img_4.setStyleSheet("image: " + cons.img_url[4])
        self.label_img_4.setText("")
        self.label_img_4.setObjectName("label_img_4")
        self.label_img_5 = QtWidgets.QLabel(self.grp_puzzle)
        self.label_img_5.setGeometry(QtCore.QRect(687, 188, 336, 178))
        self.label_img_5.setStyleSheet("image: " + cons.img_url[5])
        self.label_img_5.setText("")
        self.label_img_5.setObjectName("label_img_5")
        self.label_img_6 = QtWidgets.QLabel(self.grp_puzzle)
        self.label_img_6.setGeometry(QtCore.QRect(5, 371, 336, 178))
        self.label_img_6.setStyleSheet("image: " + cons.img_url[6])
        self.label_img_6.setText("")
        self.label_img_6.setObjectName("label_img_6")
        self.label_img_7 = QtWidgets.QLabel(self.grp_puzzle)
        self.label_img_7.setGeometry(QtCore.QRect(346, 371, 336, 178))
        self.label_img_7.setStyleSheet("image: " + cons.img_url[7])
        self.label_img_7.setText("")
        self.label_img_7.setObjectName("label_img_7")
        self.label_img_8 = QtWidgets.QLabel(self.grp_puzzle)
        self.label_img_8.setGeometry(QtCore.QRect(687, 371, 336, 178))
        self.label_img_8.setStyleSheet("image: " + cons.img_url[8])
        self.label_img_8.setText("")
        self.label_img_8.setObjectName("label_img_8")
        self.grp_photo = QtWidgets.QGroupBox(self.centralwidget)
        self.grp_photo.setGeometry(QtCore.QRect(1038, 5, 514, 314))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.grp_photo.setFont(font)
        self.grp_photo.setObjectName("grp_photo")
        self.label_img_full = QtWidgets.QLabel(self.grp_photo)
        self.label_img_full.setGeometry(QtCore.QRect(5, 20, 504, 267))
        self.label_img_full.setStyleSheet("image: " + cons.img_url[9])
        self.label_img_full.setText("")
        self.label_img_full.setObjectName("label_img_full")
        self.label_photo_info = QLinkLabel(self.grp_photo, 'https://www.fb.com/profile.php?id=100006432028774')
        self.label_photo_info.setGeometry(QtCore.QRect(5, 287, 504, 22))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label_photo_info.setFont(font)
        self.label_photo_info.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_photo_info.setAlignment(QtCore.Qt.AlignCenter)
        self.label_photo_info.setObjectName("label_photo_info")
        self.grp_instructions = QtWidgets.QGroupBox(self.centralwidget)
        self.grp_instructions.setGeometry(QtCore.QRect(1040, 374, 514, 185))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.grp_instructions.setFont(font)
        self.grp_instructions.setObjectName("grp_instructions")
        self.text_instructions = QtWidgets.QTextBrowser(self.grp_instructions)
        self.text_instructions.setGeometry(QtCore.QRect(5, 20, 504, 120))
        self.text_instructions.setObjectName("text_instructions")
        self.btn_show_graph = QtWidgets.QPushButton(self.grp_instructions)
        self.btn_show_graph.setGeometry(QtCore.QRect(347, 145, 162, 35))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_show_graph.setFont(font)
        self.btn_show_graph.setToolTipDuration(-1)
        self.btn_show_graph.setObjectName("btn_show_graph")
        self.grp_btn = QtWidgets.QGroupBox(self.centralwidget)
        self.grp_btn.setGeometry(QtCore.QRect(1040, 324, 514, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.grp_btn.setFont(font)
        self.grp_btn.setTitle("")
        self.grp_btn.setObjectName("grp_btn")
        self.btn_slove_ids = QtWidgets.QPushButton(self.grp_btn)
        self.btn_slove_ids.setGeometry(QtCore.QRect(5, 5, 162, 35))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_slove_ids.setFont(font)
        self.btn_slove_ids.setToolTipDuration(-1)
        self.btn_slove_ids.setObjectName("btn_slove_ids")
        self.btn_slove_bfs = QtWidgets.QPushButton(self.grp_btn)
        self.btn_slove_bfs.setGeometry(QtCore.QRect(176, 5, 162, 35))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_slove_bfs.setFont(font)
        self.btn_slove_bfs.setToolTipDuration(-1)
        self.btn_slove_bfs.setObjectName("btn_slove_bfs")
        self.btn_reset_puzzle = QtWidgets.QPushButton(self.grp_btn)
        self.btn_reset_puzzle.setGeometry(QtCore.QRect(347, 5, 162, 35))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_reset_puzzle.setFont(font)
        self.btn_reset_puzzle.setToolTipDuration(-1)
        self.btn_reset_puzzle.setObjectName("btn_reset_puzzle")
        self.main_window.setCentralWidget(self.centralwidget)

        self.retranslate_ui()
        self.center()
        self.update_stage()
        self.set_event()
        QtCore.QMetaObject.connectSlotsByName(self.main_window)

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.main_window.setWindowTitle(_translate("main_window", "8 puzzle"))
        self.grp_photo.setTitle(_translate("main_window", "Photo"))
        self.label_photo_info.setText(_translate("main_window", "Photo by Duy Trần"))
        self.grp_instructions.setTitle(_translate("main_window", "Instructions"))
        self.btn_show_graph.setToolTip(_translate("main_window", "Show graph"))
        self.btn_show_graph.setText(_translate("main_window", "Show graph"))
        self.btn_slove_ids.setToolTip(_translate("main_window", "Solve 8 puzzle by ITERATIVE DEEPENING SEARCH algorithm"))
        self.btn_slove_ids.setText(_translate("main_window", "Solve by IDS"))
        self.btn_slove_bfs.setToolTip(_translate("main_window", "Solve 8 puzzle by BREADTH FIRST SEARCH algorithm"))
        self.btn_slove_bfs.setText(_translate("main_window", "Solve by BFS"))
        self.btn_reset_puzzle.setToolTip(_translate("main_window", "Set puzzle to initial state"))
        self.btn_reset_puzzle.setText(_translate("main_window", "Reset puzzle"))

    def set_event(self):
        self.main_window.keyPressEvent = self.key_press_event
        self.btn_slove_ids.clicked.connect(self.btn_slove_ids_clicked)
        self.btn_slove_bfs.clicked.connect(self.btn_slove_bfs_clicked)
        self.btn_reset_puzzle.clicked.connect(self.btn_reset_puzzle_clicked)
        self.btn_show_graph.clicked.connect(self.btn_show_graph_clicked)

    def update_stage(self):
        '''
        Set image by stage
        '''
        label_img = [self.label_img_0,
                     self.label_img_1,
                     self.label_img_2,
                     self.label_img_3,
                     self.label_img_4,
                     self.label_img_5,
                     self.label_img_6,
                     self.label_img_7,
                     self.label_img_8]

        i = 0
        for lb in label_img :
            lb.setStyleSheet("image: " + cons.img_url[self.puzzle_stage[i]])
            i = i + 1

    def turn_left(self):
        zero_index = self.puzzle_stage.index(0)
        if (zero_index % 3 > 0) :
            self.puzzle_stage = Functions.swap_list(self.puzzle_stage, zero_index, zero_index - 1)
            self.update_stage()
    
    def go_up(self):
        zero_index = self.puzzle_stage.index(0)
        if (zero_index > 2) :
            self.puzzle_stage = Functions.swap_list(self.puzzle_stage, zero_index, zero_index - 3)
            self.update_stage()

    def turn_right(self):
        zero_index = self.puzzle_stage.index(0)
        if (zero_index % 3 < 2) :
            self.puzzle_stage = Functions.swap_list(self.puzzle_stage, zero_index, zero_index + 1)
            self.update_stage()

    def go_down(self):
        zero_index = self.puzzle_stage.index(0)
        if (zero_index < len(self.puzzle_stage) - 3) :
            self.puzzle_stage = Functions.swap_list(self.puzzle_stage, zero_index, zero_index + 3)
            self.update_stage()

    def key_press_event(self, event: QtGui.QKeyEvent):
        if event.key() == Qt.Key_A:
            self.turn_left()
        elif event.key() == Qt.Key_W:
            self.go_up()
        elif event.key() == Qt.Key_D:
            self.turn_right()
        elif event.key() == Qt.Key_S:
            self.go_down()

        if (Problem.goal_state == self.puzzle_stage):
            QMessageBox.question(self.main_window, 'Success', 'Problem solved', QMessageBox.Yes)
            self.grp_btn.setDisabled(True)
        else :
            self.grp_btn.setDisabled(False)


    def action(self, solution):
        self.grp_btn.setDisabled(True)
        self.text_instructions.setText('')
        time_delay = 0
        
        for action in solution:
            if (action != '') :
                QMessageBox.question(self.main_window, 'Action', action + '\t', QMessageBox.Yes)
                str = self.text_instructions.toPlainText()
                self.text_instructions.setText(str + action + '\n')

            if (action == 'LEFT') : 
                self.turn_left()
            elif (action == 'UP') :
                self.go_up()
            elif (action == 'RIGHT') :
                self.turn_right()
            elif (action == 'DOWN') : 
                self.go_down()

        QMessageBox.question(self.main_window, 'Success', 'Problem solved', QMessageBox.Yes)
        self.grp_btn.setDisabled(False)

    def btn_slove_ids_clicked(self):
        my_problem = Problem(self.puzzle_stage)
        solution = iterative_deepening_search_multi_thread(my_problem)
        self.action(solution.split('-'))
    
    def btn_slove_bfs_clicked(self):
        my_problem = Problem(self.puzzle_stage)
        solution = breadth_first_search(my_problem)
        self.action(solution.split('-'))
    
    def btn_reset_puzzle_clicked(self):
        self.puzzle_stage = [3, 1, 2, 6, 0, 8, 7, 5, 4]
        self.update_stage()

    def btn_show_graph_clicked(self):
        if (self.text_instructions.toPlainText() != ''):
            instructions = self.text_instructions.toPlainText()
            Functions.show_graph(instructions.split('\n'))