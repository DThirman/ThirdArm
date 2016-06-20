from sklearn import svm
import numpy as np
import serial
from sklearn.neighbors.nearest_centroid import NearestCentroid

def removeMag(line):
	return line[6:]

x = []
y = []
small = False
#clf = svm.LinearSVC()
clf = NearestCentroid()
folder = "gyro_side\\"
files = ['still.csv', 'yes.csv', 'no.csv']
for i in range(3):
	f =open(folder+files[i], 'r')

	for line in f.readlines():
		#print line
		
		line = [int(a) for a in line.split(',')]
		lines = [removeMag(line[9*j:9*j+9]) for j in range(9)]
		# smallLine=[]
		# for j in range(5):
			
			# smallLine = smallLine + line[6*j:6*j+3]
		# if small:
			# line=smallLine
		# if len(x)==0:
			# x= np.array(np.array([line]))
		# else:
			# x=np.append(x,np.array([line]), axis=0)
			# #print np.shape(x)
		x += [reduce(lambda x,y: x+y, lines[:5], [])]
		y += [i]
		x += [reduce(lambda x,y: x+y, lines[4:], [])]
		y += [i]
		
		try:
			z=1
		except Exception as e:
			#print e
			print i, line
			#z=1/0
		
	f.close()	

print len(x), len(x[0])
print len(y)
x= np.array([np.array(z) for z in x])
y = np.array(y)
print y
print np.shape(y)
print np.shape(x)
print type(x[0]), np.array(x[0])
clf.fit(x,y)
print clf
z
data = np.array([])
print "Starting to read"
for i in range(5):
	line = ser.readline()[:-2]
	line = removeMag([int(a) for a in line.split(',')])
	if small:
		line = smallLine
	data = np.append(data, np.array(line))
	
prevs = [0,0]
while True:
	#fullLine = reduce(lambda a,b: a+b, data, [])
	#print data
	#print data
	p = clf.predict(np.array(data))
	if p !=0:
		prevs[p-1] += 1
	if p == 0:
		if (prevs[0] > 2 or prevs[1] > 5):
			if prevs[0] > prevs[1]:
				print "Yes"
			else:
				print "No"
		prevs = [0,0]
	line = ser.readline()[:-2]
	line = removeMag([int(a) for a in line.split(',')])
	smallLine = line[0:3]
	if small:
		line = smallLine
	#data = np.append(data[(3 if small else 6):],np.array([line]))
	data = np.append(data[len(removeMag([[]]*9)):],np.array([line]))