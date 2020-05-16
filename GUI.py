import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget,
                             QVBoxLayout, QHBoxLayout,
                             QLabel, QPushButton, QLineEdit)


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pig Latin Converter")

        self.build_objects()
        self.position_objects()

    def build_objects(self):
        pass

    def position_objects():
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec_()
