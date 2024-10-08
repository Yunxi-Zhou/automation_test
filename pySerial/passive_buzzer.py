import serial
import time

#Arduino serial port
arduino_port = '/dev/cu/usbmodem1101'
baud_rate = 9600
timeout = 1

#initialize the serial port
ser = serial.Serial(arduino_port, baud_rate, timeout = timeout)

def read_passive():
    while True:
        return ser.readline().decode('utf-8').strip()

def main():
    try:
        read_passive()
    except KeyboardInterrupt:
        print('Exiting...')
    finally:
        ser.close()

if __name__ == '__main__':
    main()