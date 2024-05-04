from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QWidget, QPushButton
import sys

class MyWindo(QWidget):
    def __init__(self):
        super(MyWindo, self).__init__()
        self.setGeometry(20,20,500,300)
        self.setWindowTitle("Main Window")
        self.input = QLineEdit(self)
        self.input.move(200,200)
        self.b1 = QPushButton("clik me", self)
        self.b1.setText("Ok")
        self.b1.move(300,200)
        self.b1.setStyleSheet("background-color:white; width:30px;height: 30px; color:black;")
        self.b1.clicked.connect(self.fun)
        self.lab = QLabel(self)
        self.lab.move(20,40)

    def fun(self):

        print(self.input.text())
        self.lab.setText(self.input.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindo()
    win.show()

    sys.exit(app.exec_())
