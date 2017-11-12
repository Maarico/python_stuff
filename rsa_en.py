e=int(input("input e: "))
N=int(input("input N: "))
m=int(input("input message: "))
print("encoding...")
i=0
t=1
while i<e:
	t=t*m%N
	i+=1
	if i%10000000==0:
		print(str(100*i/e)+"% done" )
print(t)