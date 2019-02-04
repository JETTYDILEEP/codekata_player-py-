n=int(input())
l=[int(x) for x in input().split()]
t=[]
if(len(l)==n):
  for i in range(0,n):
    if(l[i]<n):
      t.append(l[i])
    else:
      continue
t.sort()
print(*t,sep=' ')    
