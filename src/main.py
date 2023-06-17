from measure import Sensor
from connect import do_connect
from secrets import secrets_wifi
from time import sleep
from dashboard import Dashboard
from machine import Pin

led = Pin("LED", Pin.OUT)

# Frequency of updates, in seconds.
FREQUENCY = 60

# Turning the onboard led on.
led.on()

# Connecting to WiFi.
try:
    ip = do_connect(secrets_wifi["ssid"], secrets_wifi["password"])
except KeyboardInterrupt:
    print("Keyboard interrupt")

# Defining sensor and dashboard objects.
sensor = Sensor()
dashboard = Dashboard()

#Connecting to the dashboard.
dashboard.connect()

try:
    
    # Looping forever, measuring and sending data.
    while True:
        sensor.measure()
        print(f"The temperature is {sensor.get_temperature()}°C")
        print(f"The humidity is {sensor.get_humidity()}%")
        
        dashboard.send_temperature(sensor.get_temperature())
        dashboard.send_humidity(sensor.get_humidity())
        
        sleep(FREQUENCY)

# Making sure to end the connection to the client if an exception is thrown.
finally:
    client.disconnect()
    led.off()
    print("Disconnected")
