n,l,r=map(int,input().split())
ar=[int(x) for x in input().split()]
t=[]
if(len(ar)==n):
  for i in range(l-1,r):
    t.append(ar[i])

print(min(t))
    
