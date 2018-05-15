import serial
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import sys
import threading

style.use('fivethirtyeight')
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

COMPORT = 'COM10'

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

db = databuffer()
db.setLife(100);
def animate(i):
    x = []
    y = []
    
    data = db.getData()
    for point in data:
        x.append(point[0])
        y.append(point[1])
    ax1.clear()
    ax1.plot(x,y)

def updateThread():
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
            data = headers[1].split(",")
            try:
                app=[float(data[0]),float(data[1])]
            except:
                print('err')
            print(app)
            db.addData(app)
        else:
            print('Unknown packet: '+headers[0])
    
try:
    arduino = serial.Serial(COMPORT,115200)
except Exception as e:
    print("Check COM port number: " + str(e))
    sys.exit()
else:
    print("Arduino connected")


time.sleep(7)
updateThread = threading.Thread(target=updateThread)
updateThread.start()
ani = animation.FuncAnimation(fig, animate, interval=75)
plt.show()



