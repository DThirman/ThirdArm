import serial
import time
import os 



import sys
file = 'gesture.txt'
print("Waiting for file to clear")
while(os.path.isfile(file)):
	pass
	
	

print "Opening serial"
ser = serial.Serial('COM3', 9600)
ser.isOpen()
print "Serial open"

print("Nod your head yes several times")
# time.sleep(1)
# print("2")
# time.sleep(1)
# print("1")
# time.sleep(1)
# print("Start")
maxZ = 0
minZ = 0


for i in range(100):
	line = [float(x) for x in ser.readline().split(",")]
	rates = line[3:]
	try:
		maxZ = max(maxZ, rates[8])
		minZ = min(minZ, rates[8])
	except:
		pass
#	time.sleep(.1)
	
	
print("Shake your head no several times")
# time.sleep(1)
# print("2")
# time.sleep(1)
# print("1")
# time.sleep(1)
# print("Start")
maxY = 0
minY = 0

for i in range(100):
	line = [float(x) for x in ser.readline().split(",")]
	rates = line[3:]
	maxY = max(maxY, rates[7])
	minY = min(minY, rates[7])
#	time.sleep(.1)
	
print maxZ, minZ, maxY, minY
print("Classifier trained, move your head as normal")
prevZ = [0]*30
prevY = [0]*30
prevGesture = False
yesCount = 0
noCount = 0

while True:
	
	sys.stdout.flush()
	line = [float(x) for x in ser.readline().split(",")]
	rates = line[3:]
	try:
		y = rates[7]
		z = rates[8]
		
		prevY = (prevY+[y])[1:]
		prevZ = (prevZ+[z])[1:]
		if(not os.path.isfile(file)):
			f=os.open(file, 'w')
			if (max(prevY) > .5*maxY and min(prevY) < .5*minY):
				sys.stdout.write("\b\b\b\b\b\b\b\b\b\b\b\bNo ")
				prevY = [0]*30
				f.write(str(2))
				prevGesture = True
				
			elif (max(prevZ) > .5*maxZ and min(prevZ) < .5*minZ ):
				prevZ = [0]*30
				sys.stdout.write("\b\b\b\b\b\b\b\b\bYes")
				f.write(str(1))
			else:
				f.write(str(0))
				sys.stdout.write("\b\b\b\b\b\b\b\b\b    ")
			f.close()
			
	except:
		pass