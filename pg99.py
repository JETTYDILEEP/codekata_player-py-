n=int(input())
s,i,l=0,0,[]
while(n!=0):
	s+=(n%10)*(2**i)
	i+=1
	n=n//10
while(s!=0):
	q=s%8
	s=s//8
	l.append(q)
l.reverse()
for i in range(len(l)):
	print(l[i],end="")
