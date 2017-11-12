import math
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
    while divisor<=math.sqrt(susp):
        if divisible(susp,divisor):
            return False
        else:
            divisor+=1
    return True
while True:
    suspect=input("number to check if prime= ")
    if float(suspect)==4:
        print("False")
    else:
        print(str(checkprime(float(suspect))))
