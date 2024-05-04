
import serial
import time
ser = serial.Serial(port='COM7', baudrate=115200)

move_list = [['0', '0', '0', '150'], ['0', '40', '0', '150'], ['40', '0', '0', '150'], ['0', '0', '40', '150'], ['0', '0', '0', '150'], ['60', '60', '60', '150'], ['80', '60', '60', '150'], ['60', '80', '60', '150'], ['60', '60', '80', '150'], ['0', '0', '0', '150'], ['60', '60', '60', '150'], ['80', '60', '60', '150'], ['60', '80', '60', '150'], ['60', '60', '80', '150'], ['0', '0', '0', '50']]
for i in move_list:
    #all_value = [x_data, y_data, z_data]
    all_value = ','.join([i[0], i[1], i[2], i[3]])
    print(f'value x,y,z : ', all_value)
    ser.write(all_value.encode())
    time.sleep(2)

"""
import serial
import time

ser = serial.Serial(port='COM7', baudrate=115200)

move_list = [['0', '0', '0', '150'], ['0', '40', '0', '150'], ['40', '0', '0', '150'], ['0', '0', '40', '150'], ['0', '0', '0', '150'], ['60', '60', '60', '150'], ['80', '60', '60', '150'], ['60', '80', '60', '150'], ['60', '60', '80', '150'], ['0', '0', '0', '150'], ['60', '60', '60', '150'], ['80', '60', '60', '150'], ['60', '80', '60', '150'], ['60', '60', '80', '150'], ['0', '0', '0', '50']]

for i in move_list:
    # Construct the string from the current list 'i'
    all_value = ','.join(i)
    print(f'value x,y,z,speed: {all_value}')
    ser.write(all_value.encode())
    time.sleep(2)
"""
'''
import serial
import time

ser = serial.Serial(port='COM7', baudrate=115200)

move_list = [['0', '0', '0', '150'], ['0', '40', '0', '150'], ['40', '0', '0', '150'], ['0', '0', '40', '150'], ['0', '0', '0', '150'], ['60', '60', '60', '150'], ['80', '60', '60', '150'], ['60', '80', '60', '150'], ['60', '60', '80', '150'], ['0', '0', '0', '150'], ['60', '60', '60', '150'], ['80', '60', '60', '150'], ['60', '80', '60', '150'], ['60', '60', '80', '150'], ['0', '0', '0', '50']]

# Construct a list of strings by joining each sublist
all_values = [','.join(move) for move in move_list]

# Join all strings in the list and encode them
data_to_send = ''.join(all_values).encode()

print("Values to send:", all_values)

# Send the data over the serial port
ser.write(data_to_send)

# Wait for a moment before exiting
time.sleep(2)

# Close the serial port
ser.close()
'''
