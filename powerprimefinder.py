import math
import os
import time
clear = lambda: os.system('cls')
counter = 1
last = 0
lastpower = 0
power = 1
def divisible(sus, div):
    sec=1
    while sec*div<sus:
        sec+=1

    if sec*div==sus:
        return(True)
    else:
        return(False)
def checkprime(susp):
    divisor=2
    while divisor<math.sqrt(susp):
        if divisible(susp,divisor):
            return False
        else:
            divisor+=1
    return True
suspect = int(math.pow(2,power)-1)
while True:
    if checkprime(suspect):
        last = suspect
        lastpower = power
        counter+=1
        time.sleep(1);
        if divisible(counter,1000):
            print("primes found:"+str(counter))   
    clear()
    print("last prime found: "+str(last))
    print("power of last prime: "+str(lastpower))
    print("last numbert checked: "+str(suspect))
    print("power of last number checked: "+str(power))
    print("number being checked: "+str(int(math.pow(2,power+1)-1)))
    power+=1
    suspect = int(math.pow(2,power)-1)
