import math
import os
clear = lambda: os.system('cls')
counter = 0
suspect = 1
def divisible(sus, div):
    return sus%div==0
def checkprime(susp):
    divisor=2
    while divisor<=math.sqrt(susp):
        if divisible(susp,divisor):
            return False
        else:
            divisor+=1
    return True
while True:
    if checkprime(suspect):
        clear()
        print("last prime found: "+str(suspect))
        counter+=1
        print("primes found:"+str(counter))
    suspect+=1
    
