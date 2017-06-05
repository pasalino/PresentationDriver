# Presentation Driver v. 1.0
# Creation Date: 14/05/2017
# Creator: Pasalino http://www.tartarugamaori.it/

import signal
import argparse
import pyautogui
import serial.tools.list_ports
import asyncio

# Serial Port
serialPort = None
loop = None

# Parsing argument
parser = argparse.ArgumentParser(description='Presentation Driver 1.0 Python Edition')
parser.add_argument('--port', '-p', dest='port', help='serial port name')
parser.add_argument('--list', '-l', dest='list', action='store_true', help='list of available serial port')
args = parser.parse_args()


# list of available port
def print_list_port():
    print("List of serial port:")
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        print(p)


# close listener on serial port
def close_listener(signal, frame):
    global serialPort
    serialPort.close()
    print('Close Presentation Driver. Bye!')
    exit(0)


@asyncio.coroutine
# open listener for serial port
def start_listen():
    try:
        data = serialPort.readline()[:-1]  # the last bit gets rid of the new-line chars
        if data:
            ss = data.decode("utf-8")
            if ss == "forward":
                press('right', 'Next Slide')
            elif ss == "back":
                press('left', 'Prev Slide')
        yield from start_listen()
    except:
        exit(-1)



def press(button, label):
    pyautogui.press(button)
    print(label)

def startRemote():
    global serialPort
    serialPort = serial.Serial(port=args.port, baudrate=9600, timeout=.1)
    signal.signal(signal.SIGINT, close_listener)
    print("Start listen remote command. Open presentation and use remote")

    loop = asyncio.get_event_loop()
    try:
        asyncio.async(start_listen())
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()
        close_listener()


if __name__ == "__main__":
    if args.list:
        print_list_port()
    elif args.port is not None:
        startRemote()
    else:
        parser.print_help()
