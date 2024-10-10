import serial
import time

# Arduino serial port
arduino_port = '/dev/cu.usbmodem1101'
baud_rate = 9600
timeout = 1

#initialize
ser = serial.Serial(arduino_port, baud_rate, timeout = timeout)

def serial_joy():
    try:
        line = ser.readline().decode('utf-8').strip()
        if line:
            print('result: ', line)
        else:
            print('No data received')
    except Exception as e:
        print(f'Error reading from serial port: {e}')
    time.sleep(3)
def main():
    try:
        while True:
            serial_joy()
    except KeyboardInterrupt:
        print('Existing...')
    finally:
        ser.close()

if __name__ == '__main__':
    main()
    
    