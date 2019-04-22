def fac(n):
	f=1
	for i in range(1,n+1):
		f=f*i
	return f
a,b,c=map(int,input().split())
x=(fact(a)//fact(b))//fact(c)
print(x)
