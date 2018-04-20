import serial
import time

arduino=serial.Serial('/dev/ttyACM1',9600)

prevData = 0

while True:
    inData = arduino.readline()
    inString = inData.decode('utf-8')
    headers = inString.split(";")
    if headers[0] == "HBT":
        data = int(headers[1])
        print(data)

        if (data-prevData) > 1:
            print("Missed beat")
        prevData = data
    
