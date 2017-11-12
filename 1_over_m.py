from decimal import *
getcontext().prec += 3
ans = 0
denom = 1
while 1==1:
    ans+=1/denom
    denom=denom*2
    print(str(ans))
