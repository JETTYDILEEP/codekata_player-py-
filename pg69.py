n,m=map(int,input().split())
l=[int(x) for x in input().split()]
if(n==len(l)):
  del l[n-m:n]

print(*l,sep=' ')   
  
