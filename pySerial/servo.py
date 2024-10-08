import serial
import time

#Arduino serial port
arduino_port = '/dev/cu.usbmodem1101'
baud_rate = 9600
timeout = 1

# initialize the serial port
ser = serial.Serial(arduino_port, baud_rate, timeout = timeout)
time.sleep(2) # wait for arduino to come online

def send_angle(angle):
    if 0 <= angle <= 180:
        ser.write(f'{angle}\n'.encode('utf-8'))
        time.sleep(0.1)
        print(f'Sent angle: {angle}')
    else:
        print('Angle out of range. Must be between 0 and 180')

def main():
    try:
        while True:
            # user input angle value
            angle = int(input('Enter servo angle (0-180): '))
            send_angle(angle)
            
            # read the return value of the Arduino
            response = ser.readline().decode('utf-8').strip()
            if response:
                print(f'Arduino says: {response}')
    except KeyboardInterrupt:
        print('Exiting...')
    finally:
        ser.close()
        
if __name__ == '__main__':
    main()
            