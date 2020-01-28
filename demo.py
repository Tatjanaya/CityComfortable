# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QInputDialog, QFileDialog, QWidget
from PyQt5.QtCore import *
import Ts
import calRes
import colormaps
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 876)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 680, 93, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(560, 680, 93, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 40, 111, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 90, 111, 31))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(200, 40, 491, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 90, 491, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(200, 290, 491, 151))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(380, 680, 93, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 290, 111, 31))
        self.label_3.setObjectName("label_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(700, 40, 61, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(700, 90, 61, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 140, 111, 31))
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 140, 491, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(700, 140, 61, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 190, 111, 31))
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(200, 190, 491, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(700, 190, 61, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(50, 240, 111, 31))
        self.label_6.setObjectName("label_6")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(200, 240, 491, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(700, 240, 61, 31))
        self.pushButton_8.setObjectName("pushButton_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "城市气候舒适度"))
        self.pushButton.setText(_translate("MainWindow", "确定"))
        self.pushButton_2.setText(_translate("MainWindow", "退出"))
        self.label.setText(_translate("MainWindow", " 地表分类路径"))
        self.label_2.setText(_translate("MainWindow", "   B10路径"))
        self.pushButton_3.setText(_translate("MainWindow", "预览"))
        self.label_3.setText(_translate("MainWindow", "   信息栏"))
        self.pushButton_4.setText(_translate("MainWindow", "选择"))
        self.pushButton_5.setText(_translate("MainWindow", "选择"))
        self.label_4.setText(_translate("MainWindow", "   B11路径"))
        self.pushButton_6.setText(_translate("MainWindow", "选择"))
        self.label_5.setText(_translate("MainWindow", "   B4路径"))
        self.pushButton_7.setText(_translate("MainWindow", "选择"))
        self.label_6.setText(_translate("MainWindow", "   B5路径"))
        self.pushButton_8.setText(_translate("MainWindow", "选择"))


class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.calResults)
        self.pushButton_2.clicked.connect(QCoreApplication.instance().quit)
        self.pushButton_3.clicked.connect(self.openFolder)
        self.pushButton_4.clicked.connect(self.openFile)
        self.pushButton_5.clicked.connect(self.openFile2)
        self.pushButton_6.clicked.connect(self.openFile3)
        self.pushButton_7.clicked.connect(self.openFile4)
        self.pushButton_8.clicked.connect(self.openFile5)

        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.lineEdit_5.setText("")
        self.textEdit.setText("欢迎使用, 选择对应波段Landsat8和地表分类图，点击确定即可运行\n出品：热红外2组")

    def openFile(self):
        filename, ok = QFileDialog.getOpenFileName(self, "选取文件", r"./", "All Files(*)")
        if ok:
            self.lineEdit.setText(str(filename))

    def openFile1(self):
        filename = QFileDialog.getExistingDirectory(self, "选取文件夹", r"./")
        self.lineEdit_2.setText(str(filename))

    def openFile2(self):
        filename, ok = QFileDialog.getOpenFileName(self, "选取文件", r"./", "All Files(*)")
        if ok:
            self.lineEdit_2.setText(str(filename))

    def openFile3(self):
        filename, ok = QFileDialog.getOpenFileName(self, "选取文件", r"./", "All Files(*)")
        if ok:
            self.lineEdit_3.setText(str(filename))

    def openFile4(self):
        filename, ok = QFileDialog.getOpenFileName(self, "选取文件", r"./", "All Files(*)")
        if ok:
            self.lineEdit_4.setText(str(filename))

    def openFile5(self):
        filename, ok = QFileDialog.getOpenFileName(self, "选取文件", r"./", "All Files(*)")
        if ok:
            self.lineEdit_5.setText(str(filename))

    def saveFile(self):
        filename = QFileDialog.getExistingDirectory(self, "文件保存", r"./datas")
        self.lineEdit_12.setText(str(filename))

    def openFolder(self):
        path = os.path.abspath('.')
        pathfolder = path + os.sep + "datas"
        os.system('explorer.exe /n, %s' % pathfolder)

    def calResults(self):
        fc = self.lineEdit.text()
        f10 = self.lineEdit_2.text()
        f11 = self.lineEdit_3.text()
        f4 = self.lineEdit_4.text()
        f5 = self.lineEdit_5.text()
        ts, wv = Ts.Ts_cal(f10, f11, f4, f5, fc)
        I_hc = calRes.Index_1(ts, wv)
        colormaps.test_gray2color()
        self.textEdit.setText(self, "运行完毕")