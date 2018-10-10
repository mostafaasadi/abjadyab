#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, \
    QLineEdit


abjad_dic = {
    'ا': 1,
    'آ': 1,
    'ب': 2,
    'پ': 2,
    'ج': 3,
    'چ': 3,
    'د': 4,
    'ه': 5,
    'و': 6,
    'ز': 7,
    'ژ': 7,
    'ح': 8,
    'ط': 9,
    'ی': 10,
    'ک': 20,
    'گ': 20,
    'ل': 30,
    'م': 40,
    'ن': 50,
    'س': 60,
    'ع': 70,
    'ف': 80,
    'ص': 90,
    'ق': 100,
    'ر': 200,
    'ش': 300,
    'ت': 400,
    'ث': 500,
    'خ': 600,
    'ذ': 700,
    'ض': 800,
    'ظ': 900,
    'غ': 1000
}


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Abjadyab'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 120
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        # Icon
        self.setWindowIcon(QIcon('icon.png'))
        # set size
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedSize(self.size())

        # center window
        frameGm = self.frameGeometry()
        screen = QApplication.desktop().screenNumber(
            QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.returnPressed.connect(self.on_click)
        self.textbox.move(20, 20)
        self.textbox.resize(280, 40)

        # Create a button in the window
        self.button = QPushButton('محاسبه', self)
        self.button.move(20, 80)

        # label
        self.lbl = QLabel(self)
        self.lbl.move(180, 83)
        newfont = QFont("vazir", 20, QFont.Bold)
        self.lbl.setFont(newfont)

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        self.textbox.setReadOnly(True)
        textboxValue = self.textbox.text()
        com = abjad(textboxValue)
        if com:
            self.lbl.setText(str(com))
        else:
            self.lbl.setText('خطا')
        self.textbox.setReadOnly(False)


# Abjad main function
def abjad(word):
    com = 0
    # remove spaces
    word = word.replace(' ', '')
    for i in word:
        try:
            com += abjad_dic[i]
        except Exception as e:
            print(e)
            return False

    return com


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
