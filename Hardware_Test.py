import modbus485
import serial as serial
import time

try:
    ser = serial.Serial(port="/dev/ttyUSB0", baudrate=9600)
except:
    print("Modbus485**", "Failed to write data")

m485 = modbus485.Modbus485(ser)

relay1_ON = [1, 6, 0, 0, 0, 255, 201, 138]
relay1_OFF = [1, 6, 0, 0, 0, 0, 137, 202]

relay2_ON = [2, 6, 0, 0, 0, 255, 201, 185]
relay2_OFF = [2, 6, 0, 0, 0, 0, 137, 249]

m485.modbus485_send(relay1_ON)
time.sleep(3)
m485.modbus485_send(relay2_ON)
time.sleep(3)

m485.modbus485_send(relay1_OFF)
time.sleep(3)
m485.modbus485_send(relay2_OFF)
time.sleep(3)

m485.modbus485_read()