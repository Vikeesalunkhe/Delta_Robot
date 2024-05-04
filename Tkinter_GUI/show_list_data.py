import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("List Display")
        self.setGeometry(100, 100, 400, 300)

        self.layout = QVBoxLayout()
        self.list_widget = QListWidget()
        self.layout.addWidget(self.list_widget)
        self.setLayout(self.layout)

        # Example list data
        self.list_data = ['Item 1', 'Item 2', 'Item 3', 'Item 4']

        # Display list data
        self.populate_list()

    def populate_list(self):
        # Clear existing items
        self.list_widget.clear()
        # Add items from the list to the QListWidget
        self.list_widget.addItems(self.list_data)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec_())
