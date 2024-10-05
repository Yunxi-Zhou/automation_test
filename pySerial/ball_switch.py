import serial
import time

# arduino serial port
arduino_port = '/dev/cu.usbmodem1101'
baud_rate = 9600
timeout = 1

#initialize serial communication
ser = serial.Serial(arduino_port, baud_rate, timeout = timeout)
time.sleep(2)

print("Connected to Arduino!")

try: 
    while True:
        # read Arduino serial data
        line = ser.readline().decode('utf-8').strip()
        if line:
            print('Arduino: ', line)
except KeyboardInterrupt:
    print('Existing...')
finally:
    ser.close()