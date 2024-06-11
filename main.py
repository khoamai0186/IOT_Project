import sys
import os
from Adafruit_IO import MQTTClient
from Hardware_Test import *
from dotenv import load_dotenv


load_dotenv()

AIO_FEED_IDs = ["nutnhan1", "nutnhan2"]
AIO_USERNAME = os.getenv("ADAFRUIT_IO_USERNAME")
AIO_KEY = os.getenv("ADAFRUIT_IO_KEY")


print(f'Using username: {AIO_USERNAME}')
print(f'Using key: {AIO_KEY}')

def connected(client):
    print("Ket noi thanh cong ...")
    for topic in AIO_FEED_IDs:
        client.subscribe(topic)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload + " , feed ID:" + feed_id)

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()


soil_temperature =[10, 3, 0, 6, 0, 1, 101, 112]
soil_moisture = [10, 3, 0, 7, 0, 1, 52, 176]
while True:
    readMoisture(client, soil_moisture)
    time.sleep(1)
    readTemperature(client, soil_temperature)
    time.sleep(1)