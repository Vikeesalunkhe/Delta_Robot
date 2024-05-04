import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication,QMainWindow, QLabel,QPushButton, QLineEdit
from PyQt5.QtGui import QFont
#import serial

#commPort = "COM7"
#ser = serial.Serial(commPort, baudrate=9600, timeout=1)

class My_Window(QWidget):
    def __init__(self):
        super(My_Window, self).__init__()
        self.setWindowTitle("Quoppo")
        self.setGeometry(200,200,800,800)
        self.initgui()


    def initgui(self):
        #Serial port label
        self.port_label = QLabel("Serial port : ",self)
        self.port_label.move(20,40)
        self.port_label.setFont(QFont('Helvetica',10))

        #User port input
        self.user_port = QLineEdit(self)
        self.user_port.move(120,40)

        #connect user input Port
        self.port_button = QPushButton("Connect", self)
        self.port_button.move(260,40)
        #self.port_button.clicked.connect(self.port_connect)

        #Show Connected port label
        self.show_port = QLabel("",self)
        self.show_port.move(350,40)

    """
    def port_connect(self):
        print(self.user_port.text())
        self.show_port.setText(self.user_port.text())
        self.commPort = self.user_port.text()
        self.ser = serial.Serial(self.commPort, baudrate=9600, timeout=1)
        print("Connection succ")
        """

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = My_Window()
    win.show()
    sys.exit(app.exec_())
