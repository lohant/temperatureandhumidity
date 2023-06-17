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
