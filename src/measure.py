from dht import DHT11
from machine import Pin

class Sensor:
    def __init__(self):
        #DHT11 Constructor
        self.sensor = DHT11(Pin(27))
        
        self.temperature = None
        self.humidity = None
    
    def measure(self):
        self.sensor.measure()
        self.temperature = self.sensor.temperature()
        self.humidity = self.sensor.humidity()
    
    def get_temperature(self):
        return self.temperature
    
    def get_humidity(self):
        return self.humidity
