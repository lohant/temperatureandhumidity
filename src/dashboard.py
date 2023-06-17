import time                   # Allows use of time.sleep() for delays
from mqtt import MQTTClient   # For use of MQTT protocol to talk to Adafruit IO
import ubinascii              # Conversions between binary data and various encodings
import machine                # Interfaces with hardware components
import micropython            # Needed to run any MicroPython code
from secrets import secrets_aio

class Dashboard:
    def __init__(self):
        # Adafruit IO (AIO) configuration
        self.AIO_SERVER = "io.adafruit.com"
        self.AIO_PORT = 1883
        self.AIO_USER = secrets_aio["username"]
        self.AIO_KEY = secrets_aio["key"]
        self.AIO_CLIENT_ID = ubinascii.hexlify(machine.unique_id())
        self.AIO_TEMPERATURE_FEED = "lohant00/feeds/temperature"
        self.AIO_HUMIDITY_FEED = "lohant00/feeds/humidity"
        
        self.client = MQTTClient(self.AIO_CLIENT_ID, self.AIO_SERVER, self.AIO_PORT, self.AIO_USER, self.AIO_KEY)
        
    def connect(self):
        self.client.connect()
        
    def disconnect(self):
        self.client.disconnect()
        self.client = None
    
    # Function to publish temperature to Adafruit IO MQTT server.
    def send_temperature(self, temperature):

        try:
            self.client.publish(topic=self.AIO_TEMPERATURE_FEED, msg=str(temperature))
        except Exception as e:
            print("Failed to publish temperature!")
            
    # Function to publish humidity to Adafruit IO MQTT server.
    def send_humidity(self, humidity):

        try:
            self.client.publish(topic=self.AIO_HUMIDITY_FEED, msg=str(humidity))
        except Exception as e:
            print("Failed to publish humidity!")
