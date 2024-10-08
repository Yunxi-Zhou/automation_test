import serial
import time

# Arduino serial port
arduino_port = '/dev/cu.usbmodem1101'
baud_rate = 9600
timeout = 1

# initialize the serial port
ser = serial.Serial(arduino_port, baud_rate, timeout = timeout)
time.sleep(2)

def serial_ultrasonic():
    try:
        # read the serial port
        line = ser.readline().decode('utf-8').strip()
        if line:
            distance = int(line)
            if 0 <= distance <= 500:
                print(f'result -> distance: {distance} cm')
            else:
                print('Out of range')
    except ValueError:
        print('Invalid data received')
    

def main():
    try:
        while True:
            serial_ultrasonic()
            time.sleep(1)
    except KeyboardInterrupt:
        print('Exiting...')
    finally:
        ser.close()

if __name__ == '__main__':
    main()