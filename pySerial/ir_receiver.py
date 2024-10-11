import serial
import time

#arduino port
arduino_port = '/dev/cu.usbmodem1101'
baud_rate = 9600
timeout = 1

#initialization
ser = serial.Serial(arduino_port, baud_rate, timeout = timeout)
time.sleep(1)

def serial_ir():
    try:
        line = ser.readline().decode('utf-8').strip()
        if line:
            print('result: ', line)
        else:
            print('No data received')
    except Exception as e:
        print(f'Error reading from the arduino port: {e}')
    time.sleep(3)

def main():
    try:
        while True:
            serial_ir()
    except KeyboardInterrupt:
        print('Exiting...')
    finally:
        ser.close()

if __name__ == '__main__':
    main()