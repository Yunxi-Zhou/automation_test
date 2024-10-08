import serial
import time

#Arduino serial port
arduino_port = '/dev/cu.usbmodem1101'
baud_rate = 9600
timeout = 1

# initialize the arduino serial port
ser = serial.Serial(arduino_port, baud_rate, timeout = timeout)

def read_photocell_data():
    while True:
        # read the data from the arduino serial
        if ser.in_waiting > 0: # check the waiting data is read or not
            data = ser.readline().decode('utf-8', errors = 'ignore').strip()
            print('Photocell reading: ', data)
        
        # add the delay time
        time.sleep(0.1)
        
def main():
    time.sleep(2) # wait for the initialization of the arduino
    read_photocell_data()

if __name__ == '__main__':
    main()
    