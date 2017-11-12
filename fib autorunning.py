d=1
while True:
    a=1
    b=1
    c=d
    if not c==0:
        while c>0:
            a+=b
            c-=1
            if c==0:
                print("fib("+str(d)+")= "+str(a))
            b+=a
            c-=1
            if c==0:
                print("fib("+str(d)+")= "+str(b))
    else:
        print("fib("+str(d)+")= "+str(1))
    d+=1
