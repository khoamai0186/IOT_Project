import struct
import serial

class Modbus485:
    def __init__(self, _rs485):
        self.rs485 = _rs485

    def modbus485_send(self, data):
        ser = self.rs485
        self.modbus485_clear_buffer()
        try:
            ser.write(serial.to_bytes(data))
        except Exception as e:
            print("Modbus485**", "Failed to write data:", e)
            return 0
        return
    
    def modbus485_read(self):
        ser = self.rs485
        bytesToRead = ser.inWaiting()
        if bytesToRead > 0:
            out = ser.read(bytesToRead)
            data_array = [b for b in out]
            print("Received Data:", data_array)
            return data_array
        return []
    
    def modbus485_clear_buffer(self):
        ser = self.rs485
        bytesToRead = ser.inWaiting()
        if bytesToRead > 0:
            out = ser.read(bytesToRead)
            print("Buffer: ", out)

    def modbus485_read_adc(self):
        ser = self.rs485
        bytesToRead = ser.inWaiting()
        if bytesToRead > 0:
            out = ser.read(bytesToRead)
            data_array = [b for b in out]
            print(data_array)
            if len(data_array) >= 7:
                array_size = len(data_array)
                value = (data_array[array_size - 4] * 256 + data_array[array_size - 3])/100
                return value
            else:
                return 400
        return 400
    
    

        