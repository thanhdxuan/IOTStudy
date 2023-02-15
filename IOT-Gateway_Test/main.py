import sys
import random
import time
from Adafruit_IO import MQTTClient

AIO_FEED_ID = "bbc-led-test"
AIO_USER_NAME = "thanhdauxuan"
AIO_KEY = "aio_MTZu22xtkuA392moPf1YTIUwsoeT"


#functions
def connected(client):
   print("Ket not thanh cong ...")
   client.subscribe(AIO_FEED_ID)

def subscribe(client, userdata, mid, granted_os):
   print("Subscribe thanh cong ...")

def disconnected(client):
   print("Ngat ket not ...")
   sys.exit(1)

def message(client, feed_id, payload):
   print("Nhan du lieu: " + payload)

#gateway config
client = MQTTClient(AIO_USER_NAME, AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_subscribe = subscribe
client.on_message = message
client.connect()
client.loop_background()

while True:
   value = random.randint(30, 40)
   print("Cap nhat: ", value)
   client.publish("bbc-temp-test", value)
   time.sleep(5)