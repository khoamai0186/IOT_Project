import modbus485
import serial as serial
import time

try:
    ser = serial.Serial(port="/dev/ttyUSB0", baudrate=9600)
except:
    print("Modbus485**", "Failed to write data")

m485 = modbus485.Modbus485(ser)

relay1_ON  = [1, 6, 0, 0, 0, 255, 201, 138]
relay1_OFF = [1, 6, 0, 0, 0, 0, 137, 202]

relay2_ON  = [2, 6, 0, 0, 0, 255, 201, 185]
relay2_OFF = [2, 6, 0, 0, 0, 0, 137, 249]

relay3_ON  = [3, 6, 0, 0, 0, 255, 200, 104]
relay3_OFF = [3, 6, 0, 0, 0, 0, 136, 40]

relay4_ON  = [4, 6, 0, 0, 0, 255, 201, 223]
relay4_OFF = [4, 6, 0, 0, 0, 0, 137, 159]

relay5_ON  = [5, 6, 0, 0, 0, 255, 200, 14]
relay5_OFF = [5, 6, 0, 0, 0, 0, 136, 78]

relay6_ON  = [6, 6, 0, 0, 0, 255, 200, 61]
relay6_OFF = [6, 6, 0, 0, 0, 0, 136, 125]

relay7_ON  = [7, 6, 0, 0, 0, 255, 201, 236]
relay7_OFF = [7, 6, 0, 0, 0, 0, 137, 172]

relay8_ON  = [8, 6, 0, 0, 0, 255, 201, 19]
relay8_OFF = [8, 6, 0, 0, 0, 0, 137, 83]

soil_temperature =[10, 3, 0, 6, 0, 1, 101, 112]
soil_moisture = [10, 3, 0, 7, 0, 1, 52, 176]



def setKali(state):
    if state == "1":
        m485.modbus485_send(relay1_ON)
        print("Mo binh chua phan Kali")
    else:
        m485.modbus485_send(relay1_OFF)
        print("Dong binh chua phan Kali")
    time.sleep(1)
    m485.modbus485_read()

def setH2O(state):
    if state == "1":
        m485.modbus485_send(relay2_ON)
        print("Mo binh chua nuoc")
    else:
        m485.modbus485_send(relay2_OFF)
        print("Dong binh chua nuoc")
    time.sleep(1)
    m485.modbus485_read()

def setMg(state):
    if state == "1":
        m485.modbus485_send(relay3_ON)
        print("Mo binh chua phan Mg")
    else:
        m485.modbus485_send(relay3_OFF)
        print("Dong binh chua phan Mg")
    time.sleep(1)
    m485.modbus485_read()

def setPhanLan(state):
    if state == "1":
        m485.modbus485_send(relay4_ON)
        print("Mo binh chua phan Lan")
    else:
        m485.modbus485_send(relay4_OFF)
        print("Dong binh chua phan Lan")
    time.sleep(1)
    m485.modbus485_read()

def setMixer(state):
    if state == "1":
        m485.modbus485_send(relay5_ON)
        print("Mo binh tron phan")
    else:
        m485.modbus485_send(relay5_OFF)
        print("Dong binh tron phan")
    time.sleep(1)
    m485.modbus485_read()

def setArea1(state):
    if state == "1":
        m485.modbus485_send(relay6_ON)
        print("Mo khu vuc 1")
    else:
        m485.modbus485_send(relay6_OFF)
        print("Dong khu vuc 1")
    time.sleep(1)
    m485.modbus485_read()

def setArea2(state):
    if state == "1":
        m485.modbus485_send(relay7_ON)
        print("Mo khu vuc 2")
    else:
        m485.modbus485_send(relay7_OFF)
        print("Dong khu vuc 2")
    time.sleep(1)
    m485.modbus485_read()

def setArea3(state):
    if state == "1":
        m485.modbus485_send(relay8_ON)
        print("Mo khu vuc 3")
    else:
        m485.modbus485_send(relay8_OFF)
        print("Dong khu vuc 3")
    time.sleep(1)
    m485.modbus485_read()


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
    # serial_read_data(ser)
    ser.write(soil_temp)
    time.sleep(1)
    data1 = serial_read_data(ser)
    client.publish("temp", data1)
    print("Nhiet Do: ", data1, "oC")


def readMoisture(client, soil_mois):
    # serial_read_data(ser)
    ser.write(soil_mois)
    time.sleep(1)
    data2 = serial_read_data(ser)
    client.publish("humid", data2)
    print("Do am: ", data2, "%")



# m485.modbus485_read()

