import os
clear = lambda: os.system('cls')
pi = 0;
den = 1;
switcher =1;
while 1==1:
    #for x in range(0,1):
        pi+=switcher*4/den;
        den+=2;
        switcher*=-1;
        #clear();
        print(str(pi));
