import serial
import time

# Arduino serial port
arduino_port = '/dev/cu.usbmodem1101'
baud_rate = 9600
timeout = 1

# initialize the serial port connection
ser = serial.Serial(arduino_port, baud_rate, timeout = timeout)

def send_led_data(data):
    # send a byte data to the Arduino
    ser.write(bytes([data]))
    # read the return state of the Arduino return
    feedback = ser.readline().decode('utf-8').strip()
    print('Arduino:', feedback)
# wait for the Arduino initialization
time.sleep(2)

# main, send different binary data to the Arduino to control the led light
try:
    # test data
    test_data = [0b00000000, # All led off
                 0b11111111, # All led on
                 0b10101010, # replace on and off
                 0b01010101, # replace off and on (reverse)
                 0b11001100, # 分组
                 0b11110000, # half light on and half light off
                 0b00001111] # half light off and half light on
    for data in test_data:
        send_led_data(data) #send the data to Arduino
        time.sleep(1)
except KeyboardInterrupt:
    print('Test end')
finally:
    ser.close()        