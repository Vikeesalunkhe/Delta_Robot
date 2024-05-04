from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QComboBox, QWidget
import sys
import serial
from serial.tools import list_ports

commPort = "COM7"
ser = serial.Serial(commPort, baudrate=9600, timeout=1)

class My_Windo(QWidget):
    def __init__(self):
        super(My_Windo, self).__init__()
        self.setGeometry(100,100, 300,300)
        self.setWindowTitle("main windo")
        self.initGUI()

    def initGUI(self):
        self.b1 = QPushButton(self)
        self.b1.setText("TurnOn")
        self.b1.clicked.connect(self.turnOnLED)
        self.b1.move(200,100)

        self.b2 = QPushButton(self)
        self.b2.setText("TurnOn")
        self.b2.clicked.connect(self.turnofLED)
        self.b2.move(200,200)

        self.user = QLineEdit(self)
        self.user.move(50, 50)
        self.delay_value = self.user.text()

        self.move = QPushButton("MOVE", self)
        self.move.move(50, 100)
        self.move.clicked.connect(self.time)

    def turnOnLED(self):
        ser.write(b'o')

    def turnofLED(self):
        ser.write(b'x')

    def time(self):
        Del_value = self.user.text()
        print(Del_value)
        ser.write(Del_value.encode())
        pass

if __name__ == '__main__':

    app = QApplication(sys.argv)
    win = My_Windo()

    win.show()
    sys.exit(app.exec_())

