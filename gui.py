"""
Author: TwKnD
Site: github.com/TwKnD
"""

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget,
                             QVBoxLayout, QHBoxLayout,
                             QLabel, QPushButton, QPlainTextEdit)
from PyQt5 import QtCore


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

        self.b1 = QPushButton()
        self.b1.setText("Convert ->")
        self.b1.clicked.connect(self.to_pig)

        self.b2 = QPushButton()
        self.b2.setText("<- Convert")
        self.b2.clicked.connect(self.to_eng)

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
        hbox1.addWidget(self.b1)
        hbox1.addWidget(self.label_pig)
        hbox1.addWidget(self.b2)
        hbox2.addWidget(self.ed1)
        hbox2.addWidget(self.ed2)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)

        self.wid.setLayout(vbox)

    def to_pig():
        pass

    def to_eng():
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec_()