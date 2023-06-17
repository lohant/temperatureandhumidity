# Temperature and Humidity Station
This repository contains the code and the instructions on how to build a temperature and humidity station that uploads the measurements to the cloud. This project was done as a part of my participation in an Applied IoT Course (1DT305) by Linnaeus University, Sweden. This project was undertaken in June 2023.

Name: Anton Holst
Student ID: ah226ie

The estimated time required for this project is about 5 hours. This approximation is applicable to a person with prior knowledge of python and microcontrollers, as well as access to good example code for the sensor and technologies that are used in the project.

## Objective
I chose to build this project as I thought it sounded interesting and useful. The technologies and sensors involved also intrigued me. The sensor will primarily be located in a room in my appartment that I use as an office. The room is quite small and thus it is easily affected by changes in temperature. The main insight I gained from this project is the usefullness of solutions such as Adafruit IO in visualizing data.

## Material

All parts were bought at Electrokit.com. I bought them as parts in a kit, but they are available to buy seperately and that is the price that is listed.

| Part | Description | Price |
| --- | --- | --- |
| Raspberry Pi Pico WH | The microcontroller that is running the code | SEK 109 |
| Breadboard | Used to conveniently connect components and sensors | SEK 69 |
| USB A to Micro USB cord | Used to connect the microcontroller to the computer to transfer code | SEK 39 |
| DHT11 Sensor | The sensor that measures the temperature and humidity | SEK 49 |
| Male-male jumper wires | Used to connect the components on the breadboard | SEK 49 |

## Computer setup

### Flashing the Pico with MicroPython
1. The firmware is downloaded from [here](https://micropython.org/download/rp2-pico-w/).
2. The BOOTSEL button is then held down while the Pico is connected to the computer. This makes the Pico appear as an USB mass storage device on the computer.
3. The downloaded firmware is then copied onto the Pico.
4. Once the programming of the firmware is complete, the Pico automatically resets and is ready for use.

### IDE
I chose to use [Thonny](https://thonny.org/) as my IDE in this project. It is easy to use and have multiple functions that come in handy when programming microcontrollers in MicroPython.

## Putting everything together
The circuit was connected according to the diagram shown. The image of the circuit is borrowed from [here](https://github.com/iot-lnu/applied-iot/tree/master/Raspberry%20Pi%20Pico%20(W)%20Micropython/sensor-examples/P5_DHT_11_DHT_22). The process of connecting the components is straight-forward and should be easy as long as the circuit is connected according to the diagram. Three pins are required for voltage, ground and data. The operating voltage of the sensor is 3.3V to 5.5V, I use the 3.3V pin on the Pico to power the sensor. Note that if another pin is used for data, adjustments to this must be done in measure.py. This setup is suited for development. If you were to use this in production, I would recommend that you solder the components together and design a suitable case. This case could be designed in CAD and 3D-printed.
![Circuit](https://github.com/lohant/temperatureandhumidity/blob/main/circuit.png)

## Platform
I chose to use the [Adafruit IO](https://io.adafruit.com/) platform. This platform is cloud-based, easy to use and free at small scale. All these features enable rapid and cost-efficient development and prototyping.

## The code
The code consists of multiple files. The main file, main.py, that contains the logic and then there are multiple files that handles specific functionality or contains sensitive information. 

### main.py
Some of the parts of the code, and the reasoning behind it, is commented on below.


Here you are able to set the frequency of the measurements. Be cautious to not set this too frequent as this will result in an unnecessary load on the Adafruit IO servers.
```
# Frequency of updates, in seconds.
FREQUENCY = 60
```

The onboard led is turned on to indicate to you that the code actually is running.
```
# Turning the onboard led on.
led.on()
```

The microcontroller connects to internet through WiFi, using the WiFi-credentials set in secrets.py.
```
# Connecting to WiFi.
try:
    ip = do_connect(secrets_wifi["ssid"], secrets_wifi["password"])
except KeyboardInterrupt:
    print("Keyboard interrupt")
```

The main logic of the code. Appart from sending the measurements to the Adafruit Server, they are also printed.
```
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
```

## Transmitting the data / connectivity
The data is by default transmitted once a minute, this is however easy to adjust in the code. As I will be using this device inside of my home, I chose to connect the device to the internet through WiFi. The transport protocol used is MQTT, primarily due to seemless integration with Adafruit IO.

## Presenting the data
The data is visualized in a dashboard on the Adafruit IO platform. The dashboard is designed to illustrate current values as well as a history of the values in line graphs. Note that the extreme values in the line graphs are due to me exposing the sensor for unnatural situations (such as placing it in the fridge) to test it. The data is sent to the Adafruit server every minute by default, and the data is stored there for 30 days.

![Dashboard](https://github.com/lohant/temperatureandhumidity/blob/main/dashboard.png)

## Finalizing the design
This picture shows the final result. This project could be improved in multiple ways, the first thing I would do is probably solder the components together and designing a custom case for it. This would make it tougher and more compact, as well as making it look more professional. It would however not make it as modular and easy to develop further. In conclusion, this project has given me some insights into Internet of Things, and the factors to consider when designing and building a product in this domain.

![Final build](https://github.com/lohant/temperatureandhumidity/blob/main/build.png)
