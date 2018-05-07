import serial
import time
import csv

arduino=serial.Serial('com4',9600)
prevData = 0
time.sleep(5)
dataFile = open('data.csv', 'w')

with dataFile:
    while True:
        inData = arduino.readline()
        inString = inData.decode('utf-8')
        headers = inString.split(",")
        if headers[0] == "HBT":
            data = [int(headers[1])]
            print(data[0])

            if (data[0]-prevData) > 1:
                print("Missed beat")
            prevData = data[0]

        writer = csv.writer(dataFile, lineterminator='\r')
        writer.writerow(data)
