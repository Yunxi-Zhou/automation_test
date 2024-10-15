import serial
import time

# Arduino port serial
arduino_port = '/dev/cu.usbmodem1101'
baud_rate = 9600
timeout = 1

# initialization
ser = serial.Serial(arduino_port, baud_rate, timeout = timeout)
time.sleep(2)

# def
def serial_relay():
    try:
        # read
        line = ser.readline().decode('utf-8').strip()
        if line:
            print(f'Result: {line}')
        else:
            print('No data received')
    except Exception as e:
        print(f'Error reading from arduino port: {e}')
    time.sleep(2)

def main():
    try:
        while True:
            serial_relay()
    except KeyboardInterrupt:
        print('existing...')
    finally:
        ser.close()

if __name__ == '__main__':
    main()