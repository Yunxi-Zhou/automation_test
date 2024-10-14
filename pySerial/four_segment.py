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
def serial_segment(digit):
    try:
        if 0 <= digit < 16:
            ser.write(f'{digit}\n'.encode())
            print(f'Send: {digit}')
        else:
            print('Invalid digit, must between 0 and 15')
    except ValueError:
        print('Invalid input, please enter a number')
    except Exception as e:
        print(f'Error reading from arduino port: {e}')
    
    
def main():
    try:
        while True:
            user_input = input("Enter a number (0-15) to display: ")
            digit = int(user_input)
            serial_segment(digit)
    except KeyboardInterrupt:
        print('Existing...')
    finally:
        ser.close()
        
if __name__ == '__main__':
    main()
    
    