from model import *
import sys

def main() :
    init_stage = [3, 1, 2, 6, 0, 8, 7, 5, 4]

    app = QtWidgets.QApplication(sys.argv)
    ui = UIMainWindow(init_stage)
    ui.main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()