n=int(input())
l=[int(x) for x in input().split()]
d={}
for i in range(n):
	d[i]=i
for i in range(n):
  p=i
  for j in range(i+1,n):
    if l[p]>l[j]:
		    p=j
  if p!=i:
  	c=l[i]
  	l[i]=l[p]
  	l[p]=c
  print(d[i]+1,end=" ")
