import math
import os
clear = lambda: os.system('cls')
def lucasremainder(place, sus):
    a=4
    for x in range(2,place):
        a=((a*a)-2)%sus
        #clear()
        #print(str(int(round(100*(x/place),0)))+"% done")
    clear()
    return ((a*a)-2)%sus
while True:
    power=int(input("input power to check: "))
    suspect=pow(2,power)-1
    clear()
    if lucasremainder(power-1, suspect)==0 or power==2:
        print(str(suspect)+" is prime")
    else:
        print(str(suspect)+" is not prime")
    
