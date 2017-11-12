import math
import os
from decimal import *
def factorial(i):
	a=1
	b=1
	while a<=i:
		b*=a
		a+=1
	return b	
clear = lambda: os.system('clear')
n=0
sin=0
getcontext().prec = int(input("amount of digits of sin you want: "))
ang=Decimal(input("angle you want the sin of: "))/Decimal(math.pi/180)
i = int(input("terms of sum(0 if infinetly): "))
counter= 0
while counter!=i:
	sin+=Decimal(pow(ang,counter))/Decimal(factorial(counter))
	n=n+1
	counter+=1
	if(i==0):
		clear()		
		print(str(pi))
print(str(pi))
