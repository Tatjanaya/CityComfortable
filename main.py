import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtCore import QCoreApplication
import demo
import os


if __name__ == '__main__':
    isExists = os.path.exists("./datas")
    if not isExists:
        os.mkdir("./datas")
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = demo.MyMainForm()
    ui.show()
    sys.exit(app.exec_())

