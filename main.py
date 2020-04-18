import sys
from functools import partial
from PyQt5.QtWidgets import QApplication, QLineEdit, QLabel, QPushButton, QGridLayout, QWidget
from PyQt5.QtCore import Qt
from actions import *

# Use functools.partial to store the information, lambda for simple interaction

class myWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Setting grid wit margins ans spacing
        outerGridLayout = QGridLayout()
        outerGridLayout.setContentsMargins(0,0,0,0)
        outerGridLayout.setSpacing(0)
        self.setLayout(outerGridLayout)

        # Form settings
        form = QLineEdit("")
        form.setObjectName("form")
        form.setAlignment(Qt.AlignRight)
        form.returnPressed.connect(lambda: onClickCalc(form, label))
        outerGridLayout.addWidget(form, 1, 0, 1, 0)

        # Label settings
        label = QLabel()
        label.setAlignment(Qt.AlignRight)
        outerGridLayout.addWidget(label, 0, 0, 1, 0)

        # Setting the buttons
        for x in range(2, -1, -1):
            for y in range(2, -1, -1):
                n = str(x*3 + y + 1)
                button = QPushButton(n)
                button.clicked.connect(partial(onClick, n, form))
                button.setFixedSize(100, 100)
                button.setObjectName("number")
                outerGridLayout.addWidget(button, 5-x, y)

        # Setting operators buttons and actions connected
        operators1 = ["C", "sqrt", "^"]
        operators2 = ["+", "-", "x", "/"]
        operators3 = ["0", ".", "%", "="]

        for (i, op) in enumerate(operators1):
            button = QPushButton(op)
            if op == "C":
                button.clicked.connect(partial(onClickDelete, form))
            else:
                button.clicked.connect(partial(onClick, op, form))
            button.setFixedSize(100, 100)
            button.setObjectName("number")
            outerGridLayout.addWidget(button, 2, i)

        for (i, op) in enumerate(operators2):
            button = QPushButton(op)
            button.clicked.connect(partial(onClick, op, form))
            button.setFixedSize(100, 100)
            button.setObjectName("rightBar")
            outerGridLayout.addWidget(button, i+2, 3)

        for (i, op) in enumerate(operators3):
            button = QPushButton(op)
            button.setFixedSize(100, 100)

            if op == "=":
                button.setObjectName("equal")
                button.clicked.connect(partial(onClickCalc, form, label))
            else:
                button.setObjectName("number")
                button.clicked.connect(partial(onClick, op, form))
            outerGridLayout.addWidget(button, 6, i)

        self.loadStyle()

    def loadStyle(self, path="default.qss"):
        with open(path, "r") as styleSheet:
            style = styleSheet.read()
            self.setStyleSheet(style)

def main():
    app = QApplication(sys.argv)
    mainWindow = myWindow()

    mainWindow.setFixedSize(400, 700)
    mainWindow.setWindowTitle("MyCalc")
    mainWindow.show()

    app.exec_()

if __name__ == "__main__":
    main()