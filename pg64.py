n,k=map(int,input().split())
l=[int(x) for x in input().split()]
t=[]
if(len(l)==n):
  for i in range(0,n):
    if(l[i]<k):
      t.append(l[i])
    else:
      continue
print(*t,sep=' ')    
