from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QComboBox
import sys
import serial
from serial.tools import list_ports

commPort = "COM7"
ser = serial.Serial(commPort, baudrate=9600, timeout=1)

def turnOnLED():
    ser.write(b'o')

def turnofLED():
    ser.write(b'x')

def time():
    ser.write()

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


    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
