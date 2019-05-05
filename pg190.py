import math
m,n,o=map(int,input().split())
d=math.pow(m,2)+math.pow(n,2)
e=int(d)
f=math.sqrt(e)
g=int(f)
if(g==o):
	print("yes")
else:
	print("no")
