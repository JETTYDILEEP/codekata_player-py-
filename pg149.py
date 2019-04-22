def fat(n):
	f=1
	for i in range(1,n+1):
		f=f*i
	return f
a,b=map(int,input().split())
x=fat(a)//fat(b)
if(x==0):
  print('yes')
else:
  print('no')
