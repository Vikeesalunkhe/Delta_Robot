"""
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QWidget, QPushButton, QVBoxLayout, QTabWidget

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle("Main Window")
        self.setGeometry(20, 20, 500, 300)

        # Create a tab widget
        self.tab_widget = QTabWidget(self)
        self.setCentralWidget(self.tab_widget)

        # Add tabs to the tab widget
        self.tab1 = QWidget()
        self.tab_widget.addTab(self.tab1, "Tab 1")

        self.tab2 = QWidget()
        self.tab_widget.addTab(self.tab2, "Tab 2")

        # Create widgets for Tab 1
        self.input_tab1 = QLineEdit(self.tab1)
        self.input_tab1.move(200, 200)
        self.b1_tab1 = QPushButton("Click me", self.tab1)
        self.b1_tab1.move(300, 200)
        self.b1_tab1.clicked.connect(self.fun_tab1)
        self.lab_tab1 = QLabel(self.tab1)
        self.lab_tab1.move(20, 40)

        # Create widgets for Tab 2
        self.input_tab2 = QLineEdit(self.tab2)
        self.input_tab2.move(200, 200)
        self.b1_tab2 = QPushButton("Click me", self.tab2)
        self.b1_tab2.move(300, 200)
        self.b1_tab2.clicked.connect(self.fun_tab2)
        self.lab_tab2 = QLabel(self.tab2)
        self.lab_tab2.move(20, 40)

    def fun_tab1(self):
        self.data = QPushButton('sdjhs',self)
        self.data.move(100,100)
        print(self.input_tab1.text())
        self.lab_tab1.setText(self.input_tab1.text())

    def fun_tab2(self):
        print(self.input_tab2.text())
        self.lab_tab2.setText(self.input_tab2.text())

if __name__ == "__main__":
    app = QApplication([])
    win = MyWindow()
    win.show()
    app.exec_()
"""
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel, QPushButton

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window with Tab")
        self.setGeometry(100, 100, 600, 400)

        # Create the central widget for the main window
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Create a layout for the central widget
        self.central_layout = QVBoxLayout(self.central_widget)

        # Create a tab widget
        self.tab_widget = QTabWidget()

        # Add the tab widget to the central layout
        self.central_layout.addWidget(self.tab_widget)

        # Create tabs and add them to the tab widget
        self.create_tab("Tab 1", "Content of Tab 1")
        self.create_tab("Tab 2", "Content of Tab 2")
        self.create_tab("tab3", "cntent 3")

    def create_tab(self, title, content):
        # Create a new tab
        tab = QWidget()

        # Create a layout for the tab
        layout = QVBoxLayout(tab)

        # Add content to the tab
        layout.addWidget(QLabel(content))

        # Add the tab to the tab widget with the specified title
        self.tab_widget.addTab(tab, title)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
