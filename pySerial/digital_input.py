import serial
import time

arduino_port = '/dev/cu.usbmodem1101'
baud_rate = 9600
timeout = 1

ser = serial.Serial(arduino_port, baud_rate, timeout=timeout)
time.sleep(2)

print('Connected to Arduino!')

try:
    while True:
        line = ser.readline().decode('utf-8').strip()
        if line:
            print('Arduino: ',line)
except KeyboardInterrupt:
    print('Existing...')
finally:
    ser.close()