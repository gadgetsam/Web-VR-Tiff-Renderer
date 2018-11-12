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
from server import start
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
        self.currentInvert = True
        self.currentColormap = 'Greys'
        self.folder = False
        self.statusBar()

        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')

        openFile.triggered.connect(self.showDialogFile)
        self.statusBar().showMessage('Current Axis is X')
        self.yB = QtWidgets.QPushButton(self)
        self.yB.setGeometry(QtCore.QRect(90, 120, 75, 23))
        self.yB.setObjectName("yB")
        self.zB = QtWidgets.QPushButton(self)
        self.zB.setGeometry(QtCore.QRect(170, 120, 75, 23))
        self.zB.setObjectName("zB")
        self.label1b = QtWidgets.QLabel(self)
        self.label1b.setGeometry(QtCore.QRect(30, 20, 271, 31))
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
        self.folderOpenB = QtWidgets.QPushButton(self)
        self.folderOpenB .setGeometry(QtCore.QRect(90, 50, 75, 23))
        self.folderOpenB.setObjectName("folderOpenB")
        self.label1a = QtWidgets.QLabel(self)
        self.label1a.setGeometry(QtCore.QRect(10, 30, 70, 16))
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
        self.line_5.setGeometry(QtCore.QRect(10, 350, 301, 16))
        self.line_5.setStyleSheet("")
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.label5b = QtWidgets.QLabel(self)
        self.label5b.setGeometry(QtCore.QRect(30, 300, 291, 61))
        self.label5b.setStyleSheet("")
        self.label5b.setObjectName("label5b")
        self.label6b = QtWidgets.QLabel(self)
        self.label6b.setGeometry(QtCore.QRect(30, 360, 291, 90))
        self.label6b.setStyleSheet("")
        self.label6b.setObjectName("label6b")
        self.label6a = QtWidgets.QLabel(self)
        self.label6a.setGeometry(QtCore.QRect(10, 370, 47, 21))
        self.label6a.setStyleSheet("font: bold 18px;")
        self.label6a.setObjectName("label6a")
        self.line_7 = QtWidgets.QFrame(self)
        self.line_7.setGeometry(QtCore.QRect(10, 450, 301, 16))
        self.line_7.setStyleSheet("")
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.progressBar = QtWidgets.QProgressBar(self)
        self.progressBar.setGeometry(QtCore.QRect(20, 470, 271, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.invertCheckbox = QtWidgets.QCheckBox(self)
        self.invertCheckbox.setGeometry(QtCore.QRect(200, 200, 70, 17))
        self.invertCheckbox.setObjectName("invertCheckbox")
        self.invertCheckbox.setChecked(True)
        self.colorMapDropdown = QtWidgets.QComboBox(self)
        self.colorMapDropdown.setGeometry(QtCore.QRect(80, 200, 101, 22))
        self.colorMapDropdown.setObjectName("colorMapDropdown")

        cmaps = [
            'Greys','viridis', 'plasma', 'inferno', 'magma',

                      'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
                     'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
                     'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn',

                     'binary', 'gist_yarg', 'gist_gray', 'gray', 'bone', 'pink',
                     'spring', 'summer', 'autumn', 'winter', 'cool', 'Wistia',
                     'hot', 'afmhot', 'gist_heat', 'copper',
                     'PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu',
                     'RdYlBu', 'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic',
                     'Pastel1', 'Pastel2', 'Paired', 'Accent',
                     'Dark2', 'Set1', 'Set2', 'Set3',
                     'tab10', 'tab20', 'tab20b', 'tab20c',
                     'flag', 'prism', 'ocean', 'gist_earth', 'terrain', 'gist_stern',
                     'gnuplot', 'gnuplot2', 'CMRmap', 'cubehelix', 'brg', 'hsv',
                     'gist_rainbow', 'rainbow', 'jet', 'nipy_spectral', 'gist_ncar']
        for x in cmaps:
            self.colorMapDropdown.addItem(x)

        self.colorMapDropdown.activated[str].connect(self.changeColorMap)

        self.invertCheckbox.stateChanged.connect(self.changeInvert)

        self.xB.setCheckable(False)

        self.xB.clicked.connect(self.changeAxis)

        self.yB.setCheckable(False)

        self.yB.clicked.connect(self.changeAxis)

        self.zB.setCheckable(False)
        self.zB.clicked.connect(self.changeAxis)

        self.genB.clicked.connect(self.genFull)
        self.fileOpenB.setCheckable(False)
        self.fileOpenB.clicked.connect(self.showDialogFile)

        self.folderOpenB.setCheckable(False)
        self.folderOpenB.clicked.connect(self.showDialogFolder)

        # self.label = QLabel(self)
        # self.label.setGeometry(200, 40, 250, 250)
        self.setGeometry(50,50,583, 515)
        self.setWindowTitle('WebVR Tiff Renderer')
        self.xyzB = [self.xB, self.yB, self.zB]
        self.retranslateUi()
        self.show()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        # Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.yB.setText(_translate("Dialog", "Y"))
        self.zB.setText(_translate("Dialog", "Z"))
        self.label1b.setText(_translate("Dialog", "Open .tiff file or folder of .tiff files:"))
        self.fileOpenB.setText(_translate("Dialog", "Open File"))
        self.folderOpenB.setText(_translate("Dialog", "Open Folder"))
        self.label1a.setText(_translate("Dialog", "1. "))
        self.label2a.setText(_translate("Dialog", "2."))
        self.label2b.setText(_translate("Dialog", "Choose orientation of stack:"))
        self.xB.setText(_translate("Dialog", "X"))
        self.label3a.setText(_translate("Dialog", "3."))
        self.label3b.setText(_translate("Dialog", "Choose Colormap:"))
        self.genB.setText(_translate("Dialog", "Generate"))
        self.label4a.setText(_translate("Dialog", "4."))
        self.label4b.setText(_translate("Dialog", "Generate the visualization:"))
        self.label5a.setText(_translate("Dialog", "5."))
        self.label5b.setText(_translate("Dialog", "Go to localhost:8080 on your browser\n"
                                                  "Make sure to use the correct browser for your headset\n"
                                                  "(Chrome for Vive/Oculus and Edge for Windows Mixed Reality)\n"))
        self.label6b.setText(_translate("Dialog", "Click the glasses icon in the lower right hand corner \n"
                                                  "to enter VR. To bring the model towards you, hold down\n"
                                                  "the trigger and menu buttons (B button on Oculus Rift)\n"
                                                  "on the right controller at the same time. To move the \n"
                                                  "model hold the right controller’s trigger and move\n"
                                                  "your right hand in the direction you want to move the model."
                                        ))
        self.label6a.setText(_translate("Dialog", "6."))
        self.invertCheckbox.setText(_translate("Dialog", "Invert"))

    def showDialogFile(self):
        self.fname = QFileDialog.getOpenFileName(self, 'Open file', 'C:\\Users\\gadge\\Downloads\\als')[0]
        print(self.fname)
        if self.fname:
            self.folder = False
            self.reGenImage()
                # self.textEdit.setText(data)

    def showDialogFolder(self):
        self.fname = QFileDialog.getExistingDirectory(self, 'Open file', 'C:\\Users\\gadge\\Downloads\\als')

        print(self.fname)
        if self.fname:
            self.folder = True
            self.reGenImage()

    def reGenImage(self):

        if self.fname[0]:
            if self.test!= True:
                readTiff.readTiff(self.fname, onlyOneFile=True, axis=self.currentAxis, invert=self.currentInvert, colormap = self.currentColormap,folder=self.folder)






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
            readTiff.readTiff(self.fname, onlyOneFile=False, axis=self.currentAxis, updater = self.progressBar, invert=self.currentInvert, colormap = self.currentColormap,folder=self.folder)
        self.thread = threading.Thread(target=start, args=())
        self.progressBar.setValue(0)
        self.thread.daemon = True  # Daemonize thread
        self.thread.start()
        choice = QMessageBox.question(self, 'Open Vr',
                                            "Type localhost:8080 into the webbrowser of your choice",
                                            QMessageBox.Ok)

    def changeColorMap(self,text):
        self.currentColormap =text
        self.reGenImage()
    def changeInvert(self,state):
        self.currentInvert = state
        self.reGenImage()
    def changeAxis(self, pressed):

        source = self.sender()

        # source.toggle()
        if source.text() == "X":
            self.statusBar().showMessage('Current Dimension is X')
            self.currentAxis = 0
            self.reGenImage()



        if source.text() == "Y":
            # if self.currentAxis == 1:
            #     print(self.currentAxis)
                # self.xyzB[self.currentAxis].toggle()
            self.currentAxis = 1
            self.reGenImage()
            self.statusBar().showMessage('Current Dimension is Y')


        if source.text() == "Z":

            # if self.currentAxis == 2:
                # self.xyzB[self.currentAxis].toggle()
            self.currentAxis = 2
            self.reGenImage()
            self.statusBar().showMessage('Current Dimension is Z')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())