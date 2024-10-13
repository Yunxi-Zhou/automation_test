import serial
import time

#arduino port
arduino_port = '/dev/cu.usbmodem1101'
baud_rate = 9600
timeout = 1

# initialization
ser = serial.Serial(arduino_port, baud_rate, timeout = timeout)
time.sleep(1)

def serial_lcd():
    try:
        line = ser.readline().decode('utf-8').strip()
        if line:
            print(f'result: {line}')
        else:
            print('No data received')
    except Exception as e:
        print(f'Error reading from arduino port: {e}')
    time.sleep(2)

def main():
    try:
        while True:
            serial_lcd()
    except KeyboardInterrupt:
        print('Existing...')
    finally:
        ser.close()