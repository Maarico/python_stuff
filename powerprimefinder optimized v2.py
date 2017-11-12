import math
import os
clear = lambda: os.system('cls')
def divisible(a,b):
    return a%b==0
def isprime(sus):
    div=2
    while div<=math.sqrt(sus):
        if(divisible(sus,div)):
            return False
        div+=1
    return True
def lucasremainder(place, sus):
    a=4
    for x in range(2,place):
        a=((a*a)-2)%sus
        #print(str(a))
    return ((a*a)-2)%sus
power=int(input("power to start checking: "))
last="none"
lastpow="none"
counter=1
while True:
    suspect=pow(2,power)-1
    if isprime(power):        
        if lucasremainder(power-1,suspect)==0:
            last=suspect
            lastpow=power
            counter+=1
    clear()
    print("primes found: "+str(counter))
    print("last prime found: "+str(last))
    print("power of last prime:" +str(lastpow))
    print("last number checked: "+str(suspect))
    print("power of number being checked: "+str(power+1))
    print("number being checked: "+str(pow(2,power+1)-1))
    power+=1
