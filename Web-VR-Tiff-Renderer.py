#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

In this example, we select a file with a
QFileDialog and display its contents
in a QTextEdit.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
"""
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QMainWindow, QTextEdit,
                             QAction, QFileDialog, QApplication, QLabel, QProgressBar,QWidget, QPushButton, QLineEdit,
    QFrame, QApplication, QMessageBox)
from PyQt5.QtGui import QIcon, QPixmap
import PyQt5.QtGui
import sys
from main import start
import readTiff

import threading
class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.currentAxis = 0
        self.initUI()

    def initUI(self):
        self.fname= [False]
        self.thread = False
        self.test = False
        self.statusBar()

        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')

        openFile.triggered.connect(self.showDialog)
        self.statusBar().showMessage('Current Axis is X')
        self.yB = QtWidgets.QPushButton(self)
        self.yB.setGeometry(QtCore.QRect(90, 120, 75, 23))
        self.yB.setObjectName("yB")
        self.zB = QtWidgets.QPushButton(self)
        self.zB.setGeometry(QtCore.QRect(170, 120, 75, 23))
        self.zB.setObjectName("zB")
        self.label1b = QtWidgets.QLabel(self)
        self.label1b.setGeometry(QtCore.QRect(30, 20, 121, 31))
        self.label1b.setStyleSheet("")
        self.label1b.setObjectName("label1b")
        self.photo = QtWidgets.QLabel(self)
        self.photo.setGeometry(QtCore.QRect(320, 10, 256, 431))
        self.photo.setObjectName("photo")
        self.line = QtWidgets.QFrame(self)
        self.line.setGeometry(QtCore.QRect(10, 70, 301, 16))
        self.line.setStyleSheet("")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.fileOpenB = QtWidgets.QPushButton(self)
        self.fileOpenB.setGeometry(QtCore.QRect(170, 50, 75, 23))
        self.fileOpenB.setObjectName("fileOpenB")
        self.label1a = QtWidgets.QLabel(self)
        self.label1a.setGeometry(QtCore.QRect(10, 30, 47, 16))
        self.label1a.setStyleSheet("font: bold 18px;")
        self.label1a.setObjectName("label1a")
        self.label2a = QtWidgets.QLabel(self)
        self.label2a.setGeometry(QtCore.QRect(10, 90, 47, 21))
        self.label2a.setStyleSheet("font: bold 18px;")
        self.label2a.setObjectName("label2a")
        self.label2b = QtWidgets.QLabel(self)
        self.label2b.setGeometry(QtCore.QRect(30, 80, 161, 31))
        self.label2b.setStyleSheet("")
        self.label2b.setObjectName("label2b")
        self.xB = QtWidgets.QPushButton(self)
        self.xB.setGeometry(QtCore.QRect(10, 120, 75, 23))
        self.xB.setObjectName("xB")
        self.label3a = QtWidgets.QLabel(self)
        self.label3a.setGeometry(QtCore.QRect(10, 170, 47, 21))
        self.label3a.setStyleSheet("font: bold 18px;")
        self.label3a.setObjectName("label3a")
        self.label3b = QtWidgets.QLabel(self)
        self.label3b.setGeometry(QtCore.QRect(30, 160, 251, 31))
        self.label3b.setStyleSheet("")
        self.label3b.setObjectName("label3b")
        self.line_2 = QtWidgets.QFrame(self)
        self.line_2.setGeometry(QtCore.QRect(10, 150, 301, 16))
        self.line_2.setStyleSheet("")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.pushButton3a = QtWidgets.QPushButton(self)
        self.pushButton3a.setGeometry(QtCore.QRect(170, 200, 75, 23))
        self.pushButton3a.setObjectName("pushButton3a")
        self.line_3 = QtWidgets.QFrame(self)
        self.line_3.setGeometry(QtCore.QRect(10, 220, 301, 16))
        self.line_3.setStyleSheet("")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.genB = QtWidgets.QPushButton(self)
        self.genB.setGeometry(QtCore.QRect(170, 270, 75, 23))
        self.genB.setObjectName("genB")
        self.label4a = QtWidgets.QLabel(self)
        self.label4a.setGeometry(QtCore.QRect(10, 240, 47, 21))
        self.label4a.setStyleSheet("font: bold 18px;")
        self.label4a.setObjectName("label4a")
        self.label4b = QtWidgets.QLabel(self)
        self.label4b.setGeometry(QtCore.QRect(30, 230, 161, 31))
        self.label4b.setStyleSheet("")
        self.label4b.setObjectName("label4b")
        self.line_4 = QtWidgets.QFrame(self)
        self.line_4.setGeometry(QtCore.QRect(10, 290, 301, 16))
        self.line_4.setStyleSheet("")
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label5a = QtWidgets.QLabel(self)
        self.label5a.setGeometry(QtCore.QRect(10, 310, 47, 21))
        self.label5a.setStyleSheet("font: bold 18px;")
        self.label5a.setObjectName("label5a")
        self.line_5 = QtWidgets.QFrame(self)
        self.line_5.setGeometry(QtCore.QRect(10, 340, 301, 16))
        self.line_5.setStyleSheet("")
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.label5b = QtWidgets.QLabel(self)
        self.label5b.setGeometry(QtCore.QRect(30, 300, 261, 41))
        self.label5b.setStyleSheet("")
        self.label5b.setObjectName("label5b")
        self.label6b = QtWidgets.QLabel(self)
        self.label6b.setGeometry(QtCore.QRect(30, 350, 261, 41))
        self.label6b.setStyleSheet("")
        self.label6b.setObjectName("label6b")
        self.label6a = QtWidgets.QLabel(self)
        self.label6a.setGeometry(QtCore.QRect(10, 360, 47, 21))
        self.label6a.setStyleSheet("font: bold 18px;")
        self.label6a.setObjectName("label6a")
        self.line_7 = QtWidgets.QFrame(self)
        self.line_7.setGeometry(QtCore.QRect(10, 390, 301, 16))
        self.line_7.setStyleSheet("")
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.progressBar = QtWidgets.QProgressBar(self)
        self.progressBar.setGeometry(QtCore.QRect(20, 410, 271, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.xB.setCheckable(False)

        self.xB.clicked.connect(self.changeAxis)

        self.yB.setCheckable(False)

        self.yB.clicked.connect(self.changeAxis)

        self.zB.setCheckable(False)
        self.zB.clicked.connect(self.changeAxis)

        self.genB.clicked.connect(self.genFull)
        self.fileOpenB.setCheckable(False)
        self.fileOpenB.clicked.connect(self.showDialog)

        # self.label = QLabel(self)
        # self.label.setGeometry(200, 40, 250, 250)
        self.setGeometry(50,50,583, 455)
        self.setWindowTitle('File dialog')
        self.xyzB = [self.xB, self.yB, self.zB]
        self.retranslateUi()
        self.show()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        # Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.yB.setText(_translate("Dialog", "Y"))
        self.zB.setText(_translate("Dialog", "Z"))
        self.label1b.setText(_translate("Dialog", "Open .tif or .tiff file"))
        self.fileOpenB.setText(_translate("Dialog", "Open"))
        self.label1a.setText(_translate("Dialog", "1. "))
        self.label2a.setText(_translate("Dialog", "2."))
        self.label2b.setText(_translate("Dialog", "Choose orientation of stack"))
        self.xB.setText(_translate("Dialog", "X"))
        self.label3a.setText(_translate("Dialog", "3."))
        self.label3b.setText(_translate("Dialog", "Optional: Change the color map, open new color map file:"))
        self.pushButton3a.setText(_translate("Dialog", "Open"))
        self.genB.setText(_translate("Dialog", "Generate"))
        self.label4a.setText(_translate("Dialog", "4."))
        self.label4b.setText(_translate("Dialog", "Generate the visualization"))
        self.label5a.setText(_translate("Dialog", "5."))
        self.label5b.setText(_translate("Dialog", "Go to localhost:8080 on your browser of choice\n"
                                                  " Chrome for Vive/Oculus and Edge for Windows Mixed Reality"))
        self.label6b.setText(_translate("Dialog", "Click the glasses icon on the lower right hand corner\n"
                                                  " to enter VR. "))
        self.label6a.setText(_translate("Dialog", "6."))

    def showDialog(self):
        self.fname = QFileDialog.getOpenFileName(self, 'Open file', 'C:\\Users\\gadge\\Downloads\\als')
        print(self.fname)
        if self.fname[0]:
            if self.test!= True:
                readTiff.readTiff(self.fname[0], onlyOneFile=True, axis=self.currentAxis)






                pixmap = QPixmap("static/data/test/1.png")
                self.photo.setPixmap(pixmap)

            # self.resize(pixmap.width(), pixmap.height())


                self.show()
                # self.textEdit.setText(data)
    def reGenAxis(self, axis):

        if self.fname[0]:
            if self.test!= True:
                readTiff.readTiff(self.fname[0], onlyOneFile=True, axis=axis)






                pixmap = QPixmap("static/data/test/1.png")
                self.photo.setPixmap(pixmap)

            # self.resize(pixmap.width(), pixmap.height())


                self.show()
    def genFull(self, pressed):
        print("reading1")
        if self.thread:
            try:
                self.thread.end()
            except:
                pass
        if self.fname[0]:
            print("reading")
            self.statusBar().showMessage('Generating')
            readTiff.readTiff(self.fname[0], onlyOneFile=False, axis=self.currentAxis, updater = self.progressBar)
        self.thread = threading.Thread(target=start, args=())
        self.progressBar.setValue(0)
        self.thread.daemon = True  # Daemonize thread
        self.thread.start()
        choice = QMessageBox.question(self, 'Open Vr',
                                            "Type localhost:8080 into the webbrowser of your choice",
                                            QMessageBox.Ok)


    def changeAxis(self, pressed):

        source = self.sender()

        # source.toggle()
        if source.text() == "X":
            self.statusBar().showMessage('Current Dimension is X')
            self.reGenAxis(0)

            self.currentAxis = 0

        if source.text() == "Y":
            # if self.currentAxis == 1:
            #     print(self.currentAxis)
                # self.xyzB[self.currentAxis].toggle()
            self.reGenAxis(1)
            self.statusBar().showMessage('Current Dimension is Y')
            self.currentAxis = 1

        if source.text() == "Z":

            # if self.currentAxis == 2:
                # self.xyzB[self.currentAxis].toggle()
            self.reGenAxis(2)
            self.statusBar().showMessage('Current Dimension is Z')
            self.currentAxis = 2


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())