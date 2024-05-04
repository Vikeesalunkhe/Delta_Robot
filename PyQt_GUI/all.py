from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel,QLineEdit, QWidget, QVBoxLayout, QPushButton, QComboBox, QSpinBox, QTextEdit, QMenu
from PyQt5.QtGui import QFont
import sys


class MyWindo(QWidget):
    def __init__(self):
        super(MyWindo, self).__init__()
        #self.setGeometry(200,200,500,300)
        self.resize(500,300)
        self.setWindowTitle("Quoppo")
        self.initGui()

    def initGui(self):
        #set Layout
        self.setLayout(QVBoxLayout())

        #Create Label
        self.my_label = QLabel("Serial port : ",self)
        #self.my_label.setText("Serial POrt")
        self.my_label.move(10,40)
        self.my_label.setStyleSheet(''' font-size: 15px;border : 8px; background : white ''')
        #self.layout().addWidget(self.my_label)

        #USER INPUT
        self.input = QLineEdit(self)
        self.input.move(120,40)
        self.input.setText("Select Port")
        #self.layout().addWidget(PortInput)

        #create button
        self.port = QPushButton(self)
        self.port.setText("push me")
        self.port.move(230,40)
        self.port.clicked.connect(self.selectPort)

        self.Conectedlabel = QLabel(self)
        self.Conectedlabel.move(40,80)

        #create combo box
        self.my_combo = QComboBox(self)
        self.my_combo.addItem("COM1")
        self.my_combo.addItem("COM2")
        self.my_combo.addItem("COM2")
        self.my_combo.addItems(["first", "second", "third"])
        self.combolabel = QLabel(self)
        self.combolabel.move(300,300)

        #Spin box
        self.my_Spin = QSpinBox(self, value=10, maximum=100, minimum=0, singleStep=5, prefix="",suffix="%")
        self.my_Spin.move(600,600)
        self.Spin_label = QLabel(self)
        self.move(600,650)
        self.my_Spin.setFont(QFont('Helvetica',18))

        #text box
        self.my_text = QTextEdit(self, lineWrapMode = QTextEdit.FixedPixelWidth, lineWrapColumnOrWidth=40, placeholderText = "Add here", readOnly=False)
        self.my_text.move(700,700)

        #add menu


    def selectPort(self):
        print(self.input.text())
        self.Conectedlabel.setText(self.input.text())          #print Qline
        self.combolabel.setText(self.my_combo.currentText())   #print current combo
        print(self.my_Spin.value())
        print(self.my_text.toPlainText())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindo()

    # SHOE THE APP
    win.show()

    sys.exit(app.exec_())
