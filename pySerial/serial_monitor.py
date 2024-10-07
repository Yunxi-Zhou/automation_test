import serial
import time

# Arduino serial port
arduino_port = '/dev/cu.usbmodem1101'
baud_rate = 9600
timeout = 1

# initialize the serial port
ser = serial.Serial(arduino_port, baud_rate, timeout = timeout)

def send_command(command):
    ser.write(command.encode())
    time.sleep(0.1)
    response = ser.readline().decode('utf-8').strip()
    
def main():
    time.sleep(2)
    
    while True:
        user_input = input("Enter LED number (0-7) to turn on or 'x' to clear: ")
        if user_input in [str(i) for i in range(8)] + ['x']:
            send_command(user_input)
        elif user_input == 'q':
            print("Successfully logged out")
            break
        else:
            print("Invalid input. Please enter a number between 0-7 or 'x'.")
    ser.close()
    
if __name__ == '__main__':
    main()
