def fact():
    a=int(input("n! where n= "))
    print(str(a)+"! = ")
    b=1
    while a>1:
        b=b*a
        a-=1
    print(str(b))
while True:
    fact()
