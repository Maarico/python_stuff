while True:
    a=1
    b=1
    c=int(input("N="))-1
    if not c==0:
        while c>0:
            a+=b
            c-=1
            if c==0:
                print(str(a))
            b+=a
            c-=1
            if c==0:
                print(str(b))
    else:
        print(str(1))
