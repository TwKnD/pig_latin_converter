"""
Author: TwKnD
Site: github.com/TwKnD
"""

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget,
                             QVBoxLayout, QHBoxLayout,
                             QLabel, QPushButton, QPlainTextEdit)
# from PyQt5 import QtCore
# pylint: disable=missing-function-docstring
# TODO: Center info text
# TODO: Add padding around info text
# TODO: Right align 'Pig Latin' label
# TODO: Explore using frames for each hbox to reduce instance attributes.


class Window(QMainWindow):
    """
    GUI Builder
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pig Latin Converter")
        self.build_objects()
        self.position_objects()

    def build_objects(self):
        # make central widget to fill main window.
        # Box Layouts only work on QWidget, not QMainWindow
        self.wid = QWidget()
        self.setCentralWidget(self.wid)

        self.setGeometry(400, 100, 600, 400)
        info_text = "A simple Pig Latin Converter"
        self.info = QLabel(info_text)
        # self.info.alignment(QtCore.Qt.AlignCenter)

        self.but_1 = QPushButton()
        self.but_1.setText("Convert ->")
        self.but_1.clicked.connect(self.to_pig)

        self.but_2 = QPushButton()
        self.but_2.setText("<- Convert")
        self.but_2.clicked.connect(self.to_eng)

        en_text = "English"
        pig_text = "Pig Latin"
        self.label_eng = QLabel(en_text)
        self.label_pig = QLabel(pig_text)

        self.ed1 = QPlainTextEdit()
        self.ed2 = QPlainTextEdit()

    def position_objects(self):
        vbox = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()

        vbox.addWidget(self.info)
        hbox1.addWidget(self.label_eng)
        hbox1.addWidget(self.but_1)
        hbox1.addWidget(self.but_2)
        hbox1.addWidget(self.label_pig)
        hbox2.addWidget(self.ed1)
        hbox2.addWidget(self.ed2)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)

        self.wid.setLayout(vbox)

    def to_pig(self):
        text = self.ed1.toPlainText()
        self.ed2.setPlainText(self.pig_converter(text))

    def to_eng(self):
        text = self.ed2.toPlainText()
        self.ed1.setPlainText(self.english_converter(text))

    def pig_converter(self, string):
        l1 = []
        for w in string.split():
            if not w[-1].isalpha() and w[:-1].isalpha():
                l1.append(w[1:-1] + w[0] + 'ay' + w[-1])
            elif not w.isalpha():
                l1.append(w)
            else:
                l1.append(w[1:] + w[0] + 'ay')

        return ' '.join(l1).capitalize()

    def english_converter(self, string):
        l1 = []
        print('start:', string)
        for w in string.split():
            print(w)
            if w.isalpha():
                l1.append(w[-3] + w[:-3])
            elif len(w) > 3:
                l1.append(w[-4] + w[:-4] + w[-1])
            else:
                l1.append(w)
        return ' '.join(l1).capitalize()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec_()
