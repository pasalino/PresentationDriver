#Presentation Driver

##Abstract

This is a remote command use for change slide in Presentations. 
Use arduino for send a command in serial-mode to a receiver program. The receiver program, emulate arrow key press and change slide.


##Mission
This project is created for [IoT meetup Milano](https://www.meetup.com/it-IT/IoT-Meetup-Milano/)

[PoT - Tocca con mano quello che scrivi](https://www.meetup.com/it-IT/IoT-Meetup-Milano/events/240049140/)

It's a basic example to use arduino with serial

##Electrical Scheme
In docs there is an Electrical scheme for build a device
Use Fritzing for open and look how connect all components
###Components
* Arduino uno
* 1 Led Diode Red
* 1 Led Diode Blue
* 2 10K Resistor
* 1 220Ohm Resistor
* 1 100Ohm Resistor
* 2 Switch

##Usage

We can use three different receiver

* Busy waiting in Python
* Async in Python
* Async in Node.js

###Installation

####Python
Create virtualenv and install packages with command

    pip install -r Requirements_Mac.txt
    
#### Node
Move in Node.js folder and write this command in shell

    npm i

#### Arduino
* Connect Arduino via USB and load PresentationDriver.ino
* Restart Arduino

###Dependences
####Python

* Use Python 3.6 for [asyncio](https://docs.python.org/3/library/asyncio.html)
* [PyAutoGui](https://github.com/asweigart/pyautogui)
* [PySeral](https://github.com/pyserial/pyserial)

####Node.js

* [Robojs](https://github.com/marcog83/RoboJS)
* [SerialPort](https://github.com/EmergingTechnologyAdvisors/node-serialport)
##Use
Connect Arduino on usb
####Python
Launch:

    python presentation_driver.py --list
In this way get all serial port in monitor
Copy name of arduino port and launch

    python presentation_driver.py -p portName
    
For asyncio

    python presentation_driver_async.py -p portName


####Node.js
Launch:

    node app.js --list
In this way get all serial port in monitor
Copy name of arduino port and launch

    node app.js -p portName
    
    