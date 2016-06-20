import serial
import matplotlib.pyplot as plt

print "Opening serial"
ser = serial.Serial('COM3', 9600)
ser.isOpen()
print "Serial open"

x = []
y = []
z = []
magX = []
magY = []
magZ = []
t= [0]
import time
import time
ser.readline()
print "Starting"

for i in range(50):
	line = [float(c) for c in ser.readline().split(",")]
	rates = line[3:]
		
		
	t.append(t[-1]+1)
	x.append(int(rates[6]))
	y.append(int(rates[7]))
	z.append(int(rates[8]))
		# magX.append(int(line[3]))
		# magY.append(int(line[4]))
		# magZ.append(int(line[5]))
		# time.sleep(.1)
	
	#print fullLine[:-1]
	#f.write(fullLine[:-1]+"\n")
xPlot = plt.plot(t[:-1],x, label="x")
yPlot = plt.plot(t[:-1],y, label="y")
zPlot = plt.plot(t[:-1],z, label="z")
plt.legend()
plt.show()