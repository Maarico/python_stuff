import math
import os
clear = lambda: os.system('cls')
def lucasremainder(place, sus):
    a=4
    for x in range(2,place):
        a=((a*a)-2)%sus
        #print(str(a))
    return ((a*a)-2)%sus
power=3
last=2
lastpow=power
counter=1
while True:
    suspect=pow(2,power)-1
    if lucasremainder(power-1,suspect)==0:
        last=suspect
        lastpow=power
        counter+=1
    clear()
    print("primes found: "+str(counter))
    print("last prime found: "+str(last))
    print("power of last prime:" +str(lastpow))
    print("last number checked: "+str(suspect))
    print("power of last number: "+str(power))
    print("number being checked: "+str(pow(2,power+1)-1))
    power+=1
