"""from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel,QWidget, QVBoxLayout, QPushButton,QGraphicsDropShadowEffect
from PyQt5.QtGui import QColor
import sys

class HelloCore2webApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
    # Create a button
        hello_button = QPushButton('Say Hello', self)
        hello_button.setStyleSheet("background-color:white; width:300px;height: 30px; color:black; margin-top:100px;")

    # need to import
        shadow = QGraphicsDropShadowEffect()
        shadow.setColor(QColor(0, 0, 0, 150)) # Set the shadow color and opacity

        shadow.setBlurRadius(10)
        hello_button.setGraphicsEffect(shadow)
    # call to button
        hello_button.clicked.connect(self.say_hello)
    # Create a label to display the message
        self.message_label = QLabel(self)
    # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(hello_button)
        layout.addWidget(self.message_label)
        # Set the layout for the main window
        self.setLayout(layout)
        # Set up the main window
        self.setWindowTitle('Hello, Core2web')
        self.setGeometry(500, 500, 500, 500)
    def say_hello(self):
        self.message_label.setText('Hello, Core2web!')
        self.message_label.setStyleSheet("color:red; font-size:20px;margin-left:150px")
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HelloCore2webApp()
    window.show()
    sys.exit(app.exec_())"""
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QComboBox
import sys
import serial

commPort = "COM7"
ser = serial.Serial(commPort, baudrate=9600, timeout=1)

def turnOnLED():
    ser.write(b'o')

def turnofLED():
    ser.write(b'x')

def main():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(100,100, 300,300)
    win.setWindowTitle("main windo")

    b1 = QtWidgets.QPushButton(win)
    b1.setText("TurnOn")
    b1.clicked.connect(turnOnLED)
    b1.move(200,100)

    b2 = QtWidgets.QPushButton(win)
    b2.setText("TurnOn")
    b2.clicked.connect(turnofLED)
    b2.move(200,200)
    """
    my_combo = QComboBox(win)
    my_combo.addItems(["COM7","COM8"])
    my_combo.move(200,150)

    conn = QPushButton(win)
    conn.clicked.connect(connnect)
    print(my_combo.currentText())
    commPort = my_combo.currentText()
    ser = serial.Serial(commPort, baudrate=9600, timeout=1)
    print("connection Succ")"""


    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

