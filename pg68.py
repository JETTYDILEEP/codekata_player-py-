n=int(input())
l=[int(x) for x in input().split()]
c=0
if(n==len(l)):
  for i in range(n):
	  for j in range(i+1,n):
		  if (l.count(i)>1 and l[i]==l[i+1]):
			  c=c+1
	  
print(c)
