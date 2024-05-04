import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QLayout, QVBoxLayout, QSpinBox, QSlider, QTabWidget, QListWidget
from PyQt5.QtGui import QFont
import serial
import time
from serial.tools import list_ports

#commPort = "COM7"
#ser = serial.Serial(commPort, baudrate=9600, timeout=1)

class My_Window(QMainWindow):

    def __init__(self):
        super(My_Window, self).__init__()
        self.setWindowTitle("Quoppo")
        self.setGeometry(200,200,800,800)
        self.initGui()

    def initGui(self):
        self.layout = QVBoxLayout()

        '''Serial Port label'''
        self.port_label = QLabel("Serial port : ", self)
        self.port_label.move(20, 40)
        self.port_label.setFont(QFont('Helvetica', 10))

        '''User Port input'''
        self.user_port = QLineEdit(self)
        self.user_port.move(120, 40)
        self.user_port.setFixedWidth(100)  # Set width to 200 pixels
        self.user_port.setFixedHeight(25)  # Set height to 30 pixels
        self.layout.addWidget(self.user_port)

        '''Connect user input Port'''
        self.port_button = QPushButton("Connect", self)
        self.port_button.move(260, 40)
        self.port_button.clicked.connect(self.port_connect)

        '''Show Connected port label'''
        self.show_port = QLabel("",self)
        self.show_port.move(20, 90)
        self.show_port.setFont(QFont('Helvetica', 10))
        self.layout.addWidget(self.show_port)

        '''Xmm Ymm Zmm label'''
        self.Xmm = QLabel(self)
        self.Xmm.setText("X[mm]")
        self.Xmm.move(150, 100)
        self.Ymm = QLabel(self)
        self.Ymm.setText("Y[mm]")
        self.Ymm.move(250, 100)
        self.Zmm = QLabel(self)
        self.Zmm.setText("Z[mm]")
        self.Zmm.move(350, 100)

        '''Position'''
        self.position_label = QLabel(self)
        self.position_label.setText("Position : ")
        self.position_label.move(20, 100)
        self.position_label.setFont(QFont('Helvetica', 10))


        '''Position User input X,Y,Z'''
        self.X_mm_Value = QLineEdit(self)
        self.X_mm_Value.move(120, 150)
        self.X_mm_Value.setText("0")
        self.X_mm_Value.setFixedWidth(100)  # Set width to pixels
        self.X_mm_Value.setFixedHeight(25)  # Set height to pixels
        self.layout.addWidget(self.X_mm_Value)

        self.Y_mm_Value = QLineEdit(self)
        self.Y_mm_Value.move(230, 150)
        self.Y_mm_Value.setText("0")
        self.Y_mm_Value.setFixedWidth(100)
        self.Y_mm_Value.setFixedHeight(25)
        self.layout.addWidget(self.Y_mm_Value)

        self.Z_mm_Value = QLineEdit(self)
        self.Z_mm_Value.move(340, 150)
        self.Z_mm_Value.setText("0")
        self.Z_mm_Value.setFixedHeight(25)
        self.Z_mm_Value.setFixedWidth(100)

        '''Position Move Button'''
        self.position_Move_Button = QPushButton("Move", self)
        self.position_Move_Button.move(500, 140)
        self.position_Move_Button.setFixedWidth(100)
        self.position_Move_Button.setFixedHeight(50)
        self.position_Move_Button.clicked.connect(self.XYZ_Position)

        '''Velocity Spin and label'''
        self.velocity_label = QLabel('Velocity : ', self)
        self.velocity_label.move(20, 200)
        #self.velocity_label.setText("Velocity : ")
        self.velocity_label.setFont(QFont('Helvetica', 10))

        self.x_Velocity = QSpinBox(self, value=10, maximum=200, minimum=20, singleStep=5)
        self.x_Velocity.move(140, 200)
        self.x_Velocity.setFixedHeight(25)
        self.x_Velocity.setFixedWidth(50)

        '''
        self.Acceleration_label = QLabel("Acceleration :", self)
        self.Acceleration_label.move(20, 250)
        self.Acceleration_label.setFont(QFont('Helvetica', 10))

        self.y_Velocity = QSpinBox(self, value=10, maximum=100, minimum=0, singleStep=5, suffix="%")
        self.y_Velocity.setFixedWidth(50)
        self.y_Velocity.setFixedHeight(25)
        self.y_Velocity.move(140, 250)
        '''

        self.step_label = QLabel('Steps : ', self)
        self.step_label.move(20, 300)
        self.step_label.setFont(QFont('Helvetica', 10))

        self.steps = QSpinBox(self, value=10, maximum=100, minimum=0, singleStep=5, suffix="%")
        self.steps.move(140, 300)
        self.steps.setFixedHeight(25)
        self.steps.setFixedWidth(50)

        '''Jog label and Key'''
        self.jog_label = QLabel("JOG", self)
        self.jog_label.move(20,450)
        self.jog_label.setFont(QFont('Helvetica', 15))
        self.widget_width = 75
        self.widget_height = 50

        self.xPP = QPushButton("X+", self)
        self.xPP.setFixedHeight(self.widget_height)
        self.xPP.setFixedWidth(self.widget_width)
        self.xPP.move(120, 360)
        self.xPP.clicked.connect(self.x_increament_jog)

        self.yPP = QPushButton("Y+", self)
        self.yPP.setFixedHeight(self.widget_height)
        self.yPP.setFixedWidth(self.widget_width)
        self.yPP.move(120, 430)
        self.yPP.clicked.connect(self.y_increament_jog)

        self.zPP = QPushButton("Z+", self)
        self.zPP.setFixedHeight(self.widget_height)
        self.zPP.setFixedWidth(self.widget_width)
        self.zPP.move(120, 500)
        self.zPP.clicked.connect(self.z_increament_jog)

        '''minus jog key'''
        self.xmm = QPushButton("X-", self)
        self.xmm.setFixedWidth(self.widget_width)
        self.xmm.setFixedHeight(self.widget_height)
        self.xmm.move(200, 360)
        self.xmm.clicked.connect(self.x_decrement_jog)

        self.ymm = QPushButton("Y-", self)
        self.ymm.setFixedWidth(self.widget_width)
        self.ymm.setFixedHeight(self.widget_height)
        self.ymm.move(200, 430)
        self.ymm.clicked.connect(self.y_decrement_jog)

        self.zmm = QPushButton("Z-", self)
        self.zmm.setFixedWidth(self.widget_width)
        self.zmm.setFixedHeight(self.widget_height)
        self.zmm.move(200, 500)
        self.zmm.clicked.connect(self.z_decreament_jog)

        '''Slider'''
        self.slider = QSlider(self)
        self.slider.move(400,360)
        self.slider.setMaximum(75)
        self.slider.setMinimum(0)
        self.slider.setValue(0)
        self.slider.valueChanged.connect(self.Slider)
        self.slider.setFixedHeight(200)
        self.slider.setFixedWidth(30)
        self.slider.setTickPosition(QSlider.TicksBothSides)
        self.slider.setTickInterval(20)
        self.slider_Value_Show = QLineEdit(self)
        self.slider_Value_Show.move(360, 360)

        '''Create or save code'''
        self.save_point = QPushButton("Save Points", self)
        self.save_point.move(700, 150)
        self.save_point.clicked.connect(self.create_code)
        self.nested_List = []

        '''Run Code'''
        self.run_Code = QPushButton("Run Code", self)
        self.run_Code.move(700, 200)
        self.run_Code.clicked.connect(self.run_Code_final)

        self.x_updated = '0'
        self.y_updated = '0'
        self.z_updated = '0'

    def port_connect(self):
        print(self.user_port.text())
        try:
            self.commPort = self.user_port.text()
            self.ser = serial.Serial(self.commPort, baudrate=115200, timeout=1)
            self.show_port.setText("hgdhw")
            print(f"Connection {self.user_port.text()} Succ")
        except:
            print(f"{self.user_port.text()} Not Connected")
            self.show_port.setText(self.user_port.text())

    def XYZ_Position(self):
        '''
        try:
            #print(self.X_mm_Value.text())
            x_data = self.X_mm_Value.text()
            print(f"This is user x :{x_data}")
            self.ser.write(x_data.encode())
        except:
            pass

        try:
            #print(self.Y_mm_Value.text())
            y_data = self.Y_mm_Value.text()
            print(f"This is user x :{y_data}")
            self.ser.write(y_data.encode())
        except:
            pass

        try:
            #print(self.Z_mm_Value.text())
            z_data = self.Z_mm_Value.text()
            print(f"This is user x :{z_data}")
            self.ser.write(z_data.encode())
        except:
            pass
        '''
        x_data = self.X_mm_Value.text()
        y_data = self.Y_mm_Value.text()
        z_data = self.Z_mm_Value.text()
        self.velocity_data = str(self.x_Velocity.text())

        try:
            # all_value = [x_data, y_data, z_data]
            all_value = ','.join([x_data, y_data, z_data, self.velocity_data])
            print(f'value x,y,z : ', all_value)
            self.ser.write(all_value.encode())
        except:
            print("Facing Error in move all point")
            pass

    def Slider(self, Slider_value):
        self.slider_value = Slider_value
        self.x_data = str(Slider_value)
        self.y_data = str(Slider_value)
        self.z_data = str(Slider_value)
        self.velocity_data = str(self.x_Velocity.text())
        print(f"Velocity Value : ", self.x_Velocity.text())
        print(Slider_value)
        print(type(Slider_value))
        # self.slider_Value_Show.setText(Slider_value)

        try:
            # all_value = [x_data, y_data, z_data]
            all_value = ','.join([self.x_data, self.y_data, self.z_data, self.velocity_data])
            print(f'value x,y,z : ', all_value)
            self.ser.write(all_value.encode())
            self.X_mm_Value.setText(str(Slider_value))
            self.Y_mm_Value.setText(str(Slider_value))
            self.Z_mm_Value.setText(str(Slider_value))

        except:
            print("Facing Error in move all point")
            pass

    def x_increament_jog(self):
        '''
        try:
            current_value = self.X_mm_Value.text()
            print(current_value)
            # data = self.X_mm_Value.text()
            current_value_int = int(current_value)
            print(f"Increament Value of x :{current_value}")

        except:
            print("Facing error:1 During x increament")
            current_value_int = 0
        try:
            self.new_value = current_value_int + self.steps.value()
            str_new_value = str(self.new_value)
            # data = self.new_value
            self.X_mm_Value.setText(str(self.new_value))
            all_value = ','.join([str_new_value, self.y_data, self.z_data, self.velocity_data])
            print(f'value x,y,z : ', all_value)
            self.ser.write(all_value.encode())
            # self.ser.write(str(data).encode())
        except:
            print("Facing Error:2 During x increament")
            pass
        '''
        try:
            self.x_current_value = int(self.X_mm_Value.text())
            print("current x value :", self.x_current_value)
        except:
            print("facing Error:1 During x increament")
            pass
        try:
            self.x_inc_value = self.x_current_value + self.steps.value()
            self.X_mm_Value.setText(str(self.x_inc_value))
            self.x_updated = str(self.x_inc_value)
            all_value = ','.join([self.x_updated, self.y_data, self.z_data, self.velocity_data])
            self.ser.write(all_value.encode())
            print(f'value x,y,z : ', all_value)

        except:
            print("facing Error:2 During x decreament")
            pass

    def x_decrement_jog(self):
        try:
            self.x_dec_value = self.x_inc_value - self.steps.value()
            self.inc_value = self.x_dec_value
            self.x_updated= str(self.x_dec_value)
            self.X_mm_Value.setText(self.x_updated)
            print("Decreament value of x : ", self.x_dec_value)
            all_value = ','.join([self.x_updated, self.y_data, self.z_data, self.velocity_data])
            print(f'value x,y,z : ', all_value)
            self.ser.write(all_value.encode())
            # self.ser.write(str(new_value).encode())
        except:
            print("Facing Error During x decremaent")
            self.X_mm_Value.setText("0")
            pass



    def y_increament_jog(self):
        '''
        current_value = self.Y_mm_Value.text()
        try:
            data = self.Y_mm_Value.text()
            current_value_int = int(current_value)
            print(f"Increament Value of y :{data}")

        except:
            print("Facing error During y increament")
            current_value_int = 0
        try:
            self.new_value = current_value_int + self.steps.value()
            data = self.new_value
            self.Y_mm_Value.setText(str(self.new_value))
            self.ser.write(str(data).encode())
        except:
            pass
        '''
        try:
            self.y_current_value = int(self.Y_mm_Value.text())
            print("current Y value :", self.y_current_value)
        except:
            print("facing Error:1 During y increament")
            pass
        try:
            self.y_inc_value = self.y_current_value + self.steps.value()
            self.Y_mm_Value.setText(str(self.y_inc_value))
            self.y_updated = str(self.y_inc_value)
            all_value = ','.join([self.x_updated, self.y_updated, self.z_data, self.velocity_data])
            self.ser.write(all_value.encode())
            print(f'value x,y,z : ', all_value)

        except:
            print("facing Error:2 During y increament")
            pass

    def y_decrement_jog(self):
        try:
            self.y_dec_value = int(self.y_updated) - self.steps.value()
            self.y_updated = self.y_dec_value
            self.y_updated = str(self.x_dec_value)
            self.Y_mm_Value.setText(self.y_updated)
            print("Decreament value of x : ", self.y_dec_value)
            all_value = ','.join([self.x_updated, self.y_dec_valu, self.z_data, self.velocity_data])
            print(f'value x,y,z : ', all_value)
            self.ser.write(all_value.encode())
            # self.ser.write(str(new_value).encode())
        except:
            print("Facing Error During y decremaent")
            self.Y_mm_Value.setText("0")
            pass

    def z_increament_jog(self):
        try:
            self.z_current_value = int(self.Z_mm_Value.text())
            print("current x value :", self.z_current_value)
        except:
            print("facing Error:1 During z increament")
            pass

        try:
            self.z_inc_value = int(self.Z_mm_Value.text()) + self.steps.value()
            self.Z_mm_Value.setText(str(self.z_inc_value))
            self.z_updated = str(self.z_inc_value)
            all_value = ','.join([self.x_updated, self.y_updated, self.z_updated, self.velocity_data])
            self.ser.write(all_value.encode())
            print(f'value x,y,z : ', all_value)

        except:
            print("facing Error:2 During z incremaent")
            pass

    def z_decreament_jog(self):
        try:
            self.z_dec_value = int(self.Z_mm_Value.text()) - self.steps.value()
            self.z_updated= str(self.z_dec_value)
            self.Z_mm_Value.setText(self.z_updated)
            print("Decreament value of x : ", self.z_dec_value)
            all_value = ','.join([self.x_updated, self.y_updated, self.z_updated, self.velocity_data])
            print(f'value x,y,z : ', all_value)
            self.ser.write(all_value.encode())
            # self.ser.write(str(new_value).encode())
        except:
            print("Facing Error During z decremaent")
            self.Z_mm_Value.setText("0")
            pass


    def create_code(self):
        try:
            x = self.X_mm_Value.text()
            y = self.Y_mm_Value.text()
            z = self.Z_mm_Value.text()
            v = str(self.x_Velocity.text())

            user_point = []
            user_point.append(x)
            user_point.append(y)
            user_point.append(z)
            user_point.append(v)
            print("user point : ", user_point)
            self.nested_List.append(user_point)
            '''
            for user_point in user_inputs:
            elements = user_point.split()
            nested_List.append(elements)
            '''
            #self.updated_List = nested_List
            print(self.nested_List)
        except:
            print("facing Error During save point")

    def run_Code_final(self):
        try:
            for i in self.nested_List:
                print(i)
                #all_value = [x_data, y_data, z_data]
                all_value = ','.join([i[0], i[1], i[2], i[3]])
                print(f'value x,y,z : ', all_value)
                self.ser.write(all_value.encode())
                time.sleep(2)
        except:
            print("facing Error during run Code")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = My_Window()
    win.show()
    sys.exit(app.exec_())
