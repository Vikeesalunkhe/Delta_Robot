from tkinter import *
import serial
import tkinter as tk
from tkinter import PhotoImage

commPort = "COM7"
ser = serial.Serial(commPort, baudrate=9600, timeout=1)

def turnOnLED():
    ser.write(b'o')

def turnOfLED():
    ser.write(b'x')

def blinkLED():
    ser.write(b'b')

root = Tk()
root.title('Quoppo')

btn_On = tk.Button(root, text="Turn on", command=turnOnLED)
btn_On.grid(row=50, column=20)

btn_Off = tk.Button(root, text="Trun off", command=turnOfLED)
btn_Off.grid(row=100, column=50)

#BlinkState = IntVar()
chkBtn = tk.Checkbutton(root, command = blinkLED)
chkBtn
chkBtn.grid(row = 0, column =2)


root.geometry("350x350")
root.mainloop()
print("Run Sucssefully")
