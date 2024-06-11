import modbus485
import serial as serial
import time

try:
    ser = serial.Serial(port="/dev/ttyUSB0", baudrate=9600)
except:
    print("Modbus485**", "Failed to write data")

m485 = modbus485.Modbus485(ser)

# relay1_ON = [1, 6, 0, 0, 0, 255, 201, 138]
# relay1_OFF = [1, 6, 0, 0, 0, 0, 137, 202]

# relay2_ON = [2, 6, 0, 0, 0, 255, 201, 185]
# relay2_OFF = [2, 6, 0, 0, 0, 0, 137, 249]

# m485.modbus485_send(relay1_ON)
# time.sleep(3)
# m485.modbus485_send(relay2_ON)
# time.sleep(3)

# m485.modbus485_send(relay1_OFF)
# time.sleep(3)
# m485.modbus485_send(relay2_OFF)
# time.sleep(3)

def serial_read_data(ser):
    bytesToRead = ser.inWaiting()
    if bytesToRead > 0:
        out = ser.read(bytesToRead)
        data_array = [b for b in out]
        # print(data_array)
        if len(data_array) >= 7:
            array_size = len(data_array)
            value = data_array[array_size - 4] * 256 + data_array[array_size - 3]
            value = value/100
            return value
        else:
            return -1
    return 0



def readTemperature(client, soil_temp):
    serial_read_data(ser)
    ser.write(soil_temp)
    time.sleep(1)
    client.publish("temp", serial_read_data(ser))
    print("Nhiet Do: ", serial_read_data(ser), "oC")


def readMoisture(client, soil_mois):
    serial_read_data(ser)
    ser.write(soil_mois)
    time.sleep(1)
    client.publish("humid", serial_read_data(ser))
    print("Do am: ", serial_read_data(ser), "%")




# m485.modbus485_read()

