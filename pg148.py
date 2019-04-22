def fact(n):
	f=1
	for i in range(1,n+1):
		f=f*i
	return f
a,b=map(int,input().split())
x=fact(a)//fact(b)
if(x==0):
  print('yes')
else:
  print('no')
