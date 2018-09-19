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

        self.xB = QPushButton('X', self)
        self.xB.setCheckable(True)
        # self.xB.toggle()
        self.xB.move(10, 40)
        self.xB.setCheckable(False)

        self.xB.clicked.connect(self.changeAxis)

        self.yB = QPushButton('Y', self)
        self.yB.setCheckable(True)
        self.yB.move(10, 90)
        self.yB.setCheckable(False)

        self.yB.clicked.connect(self.changeAxis)

        self.zB = QPushButton('Z', self)
        self.zB.setCheckable(True)
        self.zB.move(10, 140)
        self.zB.setCheckable(False)
        self.zB.clicked.connect(self.changeAxis)
        self.genB = QPushButton('Generate', self)
        self.genB.setCheckable(True)
        self.genB.move(10, 190)

        self.genB.clicked.connect(self.genFull)
        self.progress = QProgressBar(self)
        self.progress.setValue(0)
        self.progress.setGeometry(10, 300, 475, 20)
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)
        self.label = QLabel(self)
        self.label.setGeometry(200, 40, 250, 250)
        self.setGeometry(300, 550, 490, 350)
        self.setWindowTitle('File dialog')
        self.xyzB = [self.xB, self.yB, self.zB]
        self.show()

    def showDialog(self):
        self.fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')

        if self.fname[0]:
            if self.test!= True:
                readTiff.readTiff(self.fname[0], onlyOneFile=True, axis=self.currentAxis)






                pixmap = QPixmap("static/data/test/1.png")
                self.label.setPixmap(pixmap)

            # self.resize(pixmap.width(), pixmap.height())


                self.show()
                # self.textEdit.setText(data)
    def reGenAxis(self, axis):

        if self.fname[0]:
            if self.test!= True:
                readTiff.readTiff(self.fname[0], onlyOneFile=True, axis=axis)






                pixmap = QPixmap("static/data/test/1.png")
                self.label.setPixmap(pixmap)

            # self.resize(pixmap.width(), pixmap.height())


                self.show()
    def genFull(self, pressed):
        print("reading1")
        if self.thread:
            self.thread.end()
        if self.fname[0]:
            print("reading")
            self.statusBar().showMessage('Generating')
            readTiff.readTiff(self.fname[0], onlyOneFile=False, axis=self.currentAxis, updater = self.progress)
        self.thread = threading.Thread(target=start, args=())
        self.progress.setValue(0)
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