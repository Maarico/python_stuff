import math
import os
clear = lambda: os.system('clear')
def divisible(sus, div):
    return sus%div==0
def checkprime(susp):
    if susp==1:
        return False
    divisor=2
    while divisor<=math.sqrt(susp):
        if divisible(susp,divisor):
            return False
        else:
            divisor+=1
    return True
while True:
    factorize=int(input("number to factorize: "))
    temp=factorize
    suspect=2;
    factors=[];
    n=0;
    isprime = bool(checkprime(factorize))
    output=str(factorize)
    if(not isprime):
        while suspect<=factorize and not isprime:
            if(checkprime(suspect)):
                #temp=factorize
                clear()
                print(str(temp)+"="+output)
                print("factor being checked: "+str(suspect))
                while(divisible(factorize,suspect)):
                    #print("divisible")
                    factors.append(suspect);
                    #print(str(suspect));
                    factorize=factorize/suspect;
                    isprime = bool(checkprime(factorize))
                    n+=1;
                    output=""
                    if not factorize/suspect==1:
                        for x in range(0,len(factors)):
                            if not int(factorize)==1:
                                output=output+str(factors[x])+"*"
                            else:
                                if not x==len(factors)-1:
                                    output=output+str(factors[x])+"*"
                                else:
                                    if x==len(factors)-1:
                                        output=output+str(factors[x])
                        if not int(factorize)==1:
                            output=output+str(int(factorize))
                        clear()
                        print(str(temp)+"="+output)
            suspect+=1;
        #output="";
        #for x in range(0,len(factors)-1):
        #    output=output+str(factors[x])+"*"
        #output=output+str(factors[len(factors)-1])
        #if isprime:
        #    output=output+"*"+str(int(factorize))
    else:
        clear()
        output=str(factorize);
        print(str(temp)+"="+output)
