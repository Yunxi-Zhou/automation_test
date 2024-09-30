import serial
import time

arduino_port = '/dev/cu.usbmodem1101' # device serial name
baud_rate = 9600 # baud rate = the Serial.begin in Arduino

# initialize the serial port
ser = serial.Serial(arduino_port, baud_rate, timeout = 1)

# 等待Arduino复位
time.sleep(1)

# read the Arduino serial data
try:
    while True:
        line = ser.readline().decode('utf-8').strip()
        if line:
            print("Received: ", line)
except KeyboardInterrupt:
    print("Existing...")
finally:
    ser.close()