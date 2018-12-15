x,y=map(int,input().split())
while(x!=y):
	if x>y:
		x-=y
	else :
		y-=x
print(x)
