import math
import random
import os
clear = lambda: os.system('cls')
pi=0;
n=0;
d=0;
while True:
    x=0.5-random.random()
    y=0.5-random.random()
    if x*x+y*y<0.25:
        n+=1
    d+=1
    pi=(n/d)*4
    clear()
    print("pi approximation: "+str(pi))
    print("darts thrown= "+str(d))
