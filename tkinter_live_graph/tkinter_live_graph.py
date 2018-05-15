import tkinter as tk
import serial
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import sys

style.use('fivethirtyeight')
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

COMPORT = 'COM3'

class databuffer:
    id = 1
    data = []
    lifetime = 0
    def setLife(self, x):
        self.lifetime = x-1
    def addData(self,x):
        if len(self.data)>self.lifetime:
            del self.data[0]
            self.data.append(x)
        else:
            self.data.append(x)
    def getData(self):
        return self.data
    def clcData(self):
        self.data=[]

def animate(i):
    x = []
    y = []
    
    data = databuffer.getData()
    for point in data:
        x.append(point[0])
        y.append(point[1])
    ax1.clear()
    ax1.plot(x,y)
    
try:
    arduino = serial.Serial(COMPORT,115200)
except Exception as e:
    print("Check COM port number: " + str(e))
    sys.exit()
else:
    print("Arduino connected")

time.sleep(5)

ani = animation.FuncAnimation(fig, animate, interval=100)
plt.show()

while True:
    inData = arduino.readline()                 #Read data from Arduino
    try:                                        #Try to decode bytes to string
        inString = inData.decode('utf-8')
    except:                                     #If an error occurs,
        print('Read Error')                     #print a warning
        continue                                #and then skip this iteration.
    else:                                       #Otherwise,
        headers = inString.split(";")           #split the data by delimiter
        
    if headers[0] == "DATA":                    #If a data packet is received
        data = headers[1].split(",")            #Split data by delimiter
        databuffer.addData(data)
    else:
        print('Unknown packet: '+headers[0])
    lines.append(data)                          #Append data collected this iteration to list

