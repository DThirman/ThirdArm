import time
import os 

x=0

while True:
	f=open('s.txt', 'w')
	f.write(str(x))
	print "Printing ", x
	f.close()
	while(os.path.isfile('s.txt')):
		pass
	x+=1
	