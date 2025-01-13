import serial
import time

arduino_port = '/dev/cu.usbmodem1101'
baud_rate = 9600
timeout = 1

ser = serial.Serial(arduino_port, baud_rate, timeout = timeout)
time.sleep(2)

def serial_remote():
    try:
        line = ser.readline().decode('utf-8').strip()
        if line:
            print(f'Result: {line}')
        else:
            print('No data received')
    except Exception as e:
        print(f'Error reading from arduino port: {e}')
    time.sleep(2)

def send_command(command):
    ser.write(f'{command}\n'.encode())
    print(f'Send: {command}')
        
def main():
    try:
        while True:
            user_input = input("Enter command(CW/CCW): ")
            if user_input in ['CW', 'CCW']:
                send_command(user_input)
            else:
                print('in')
    except KeyboardInterrupt:
        print('Existing..')
    finally:
        ser.close()

if __name__ == '__main__':
    main()