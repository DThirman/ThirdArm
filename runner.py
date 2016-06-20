from __future__ import print_function
from gestures import *
import time
import os

ser = serial.Serial('COM3', 9600)
ser.readline()
ser.readline()
ser.readline()
ser.readline()
ser.readline()
ser.readline()
deg = 90
degWin = 15
gest = Gestures()
a = [int(x) for x in ser.readline().split(",")[3:]]
b = [int(x) for x in ser.readline().split(",")[3:]]
c = [int(x) for x in ser.readline().split(",")[3:]]
d = [int(x) for x in ser.readline().split(",")[3:]]
e = [int(x) for x in ser.readline().split(",")[3:]]
gest.setInitialData([a,b,c,d,e])


meanX = (a[3]+b[3]+c[3]+d[3]+e[3])/5
meanY = (a[4]+b[4]+c[4]+d[4]+e[4])/5
meanZ = (a[5]+b[5]+c[5]+d[5]+e[5])/5
minX = 1000
maxX = 0
minY = 1000
maxY = 0
minZ = 1000
maxZ = 0
move = False
count = 0
while True:
	line = [float(x) for x in ser.readline().split(",")]
	rates = line[3:]
	pos = line[:3]
	norm = reduce(lambda x,y: x+y, [a*a for a in rates[6:]])**.5
	p = gest.predictGesture(rates)
	if(norm > 750):
		if p == 2:
			print("No")
			move = False
		if p == 1:
			print("Yes")
			move =  True
	file = 'speed.txt'
	if(not os.path.isfile(file)):
	#if False:
		f=open(file, 'w')
		if move:
			# #print("Direction :", "left" if pos[0]<deg else "right", " Speed: ", int(abs(pos[0]-deg)/degWin*255))
			
			x = rates[3]-meanX
			y = rates[4]-meanY
			z = rates[5]-meanZ
			x = -x/100
			y = -y/150
			if x> 0:
				x *= 3
			x = int(x)
		
			x *= 2
			
			if y> 0:
				y*= 1.5
			y*=2
			y= int(y)				
			# #f.write(str(int((pos[0]-deg)/degWin*20)))
			# #print(str(int((pos[0]-deg)/degWin*20)))
			f.write(str(x) + " " +str(y))
			print(str(x) + " " +str(y))
		else:
			# #print("Don't move")
			f.write(str(0)+" " + str(0))
			print(str(0)+" " + str(0))
		f.close()
	
	# # else:
		# # x = rates[3]-meanX
		# # y = rates[4]-meanY
		# # z = rates[5]-meanZ
		# # minX = min(x, minX)
		# # maxX = max(x, maxX)
		
		# # minY = min(y, minY)
		# # maxY = max(y, maxY)
		
		# # minZ = min(z, minZ)
		# # maxZ = max(z, maxZ)
		
		# # print(x,y,z, minX, maxX)