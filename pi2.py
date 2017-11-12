import math
import os
clear = lambda: os.system('clear')
a=0
b=1
c=1
d=0
e=0
while True:
	while e<10000000:
		a+=4/b*c
		b+=2
		c*=-1
		d+=1
		e+=1
	e=0
	clear()
	print("partial sum of "+str(d)+" terms")
	print("pi > "+str(a))
	print("pi < "+str(a+4/b*c))
	print("error < "+ str(4/b))
