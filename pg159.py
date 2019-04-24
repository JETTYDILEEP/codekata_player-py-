a,b=map(int,input().split())
v=a*b
x=bin(v)
c=0
for i in range(len(x)):
	if x[i]=='1':
		c+=1
print(c)
