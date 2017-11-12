import math
import random
def isprime(suspect):
	if(suspect==2):
		return True
	if(suspect<2):
		return False
	tester=2
	while (tester<=math.sqrt(suspect)):
		if(suspect%tester==0):
			return False
		tester+=1
	return True

def adv_eucl_alg(a,b):
	factors = []
	while True:
		counter=0
		if(b>a):
			c=a
			a=b
			b=c
		while a-b>0:
			a-=b
			counter+=1
		factors.append(counter)
		if a-b==0:
			s=1
			t=factors[len(factors)-2]
			i=3
			while i<=len(factors):
				s+=t*factors[len(factors)-i]
				i+=1
				if(i>len(factors)):
					break
				t+=s*factors[len(factors)-i]
				i+=1
			return [b,s,t]

length=int(input("lenght of primes to generate key: "))
found=False

dfound = False	


print("generating p and q")
while not found: #generating p and q
	p=1
	while not isprime(p):
		p=random.randrange(math.pow(10,length-1),math.pow(10,length))
	print("found p")
	q=1
	while not isprime(q):
		q=random.randrange(math.pow(10,length-1),math.pow(10,length))
	print("found q") 
	density=abs(math.log(p,2)-math.log(q,2))
	if(0.1<density and density<30 and p!=q):
		found=True
	else:
		print("non compatible: regenerating")



print("calculating N")
N=p*q


print("calculating phi")
phi=(p-1)*(q-1)


	
while not dfound:
	


	print("generating e")
	found=False
	while not found: #generating e
		e=random.randrange(2,phi-1)
		if(adv_eucl_alg(e,phi)[0]==1):
			found=True

			
	print("generating d")		
	d=0

	if(adv_eucl_alg(e,phi)[1]*e-adv_eucl_alg(e,phi)[2]*phi)==1:
		d=adv_eucl_alg(e,phi)[1]
	else:
		if(adv_eucl_alg(e,phi)[1]*e-adv_eucl_alg(e,phi)[2]*phi)==-1:
			d=adv_eucl_alg(e,phi)[2]

	if not d==0:
		dfound=True
	else:
		print("error! regenerating")
		

print("p = "+str(p)+" q = "+str(q)+" N = "+str(N)+" phi = "+str(phi)+" e = "+str(e)+" d = "+str(d))