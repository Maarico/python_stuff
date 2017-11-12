e=0
den=1
count=1
den2=1
while True:
    print(str(abs(e-pow(1+(1/den2),den2))))
    e+=1/den
    den*=count
    den2+=1
    count+=1
