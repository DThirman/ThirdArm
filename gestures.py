from sklearn import svm
import numpy as np
import serial
from sklearn.neighbors.nearest_centroid import NearestCentroid

class Gestures:
	def removeMag(self, line):
		return line[6:]
	
	def __init__(self):
		x = []
		y = []
		small = False
		#clf = svm.LinearSVC()
		self.clf = NearestCentroid()
		folder = "gyro_side\\"
		files = ['still.csv', 'yes.csv', 'no.csv']
		for i in range(3):
			f =open(folder+files[i], 'r')

			for line in f.readlines():
				#print line
				
				line = [int(a) for a in line.split(',')]
				lines = [self.removeMag(line[9*j:9*j+9]) for j in range(9)]
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
		x= np.array([np.array(z) for z in x])
		y = np.array(y)
		print y
		print np.shape(y)
		print np.shape(x)
		print type(x[0]), np.array(x[0])
		self.clf.fit(x,y)
		self.data = []

		#self.ser = serial.Serial('COM3', 9600)
		print "Classifier trained"
	

	def setInitialData(self, init):
		self.data = []
		for i in init:
			self.data = np.append(self.data,self.removeMag(i))
		
	def updateData(self, line):
		self.data = np.append(self.data[len(self.removeMag([[]]*9)):],np.array([self.removeMag(line)]))
		
		
		
	def predictGesture(self, line):
		self.updateData(line)
		return self.clf.predict(np.array(self.data))
		