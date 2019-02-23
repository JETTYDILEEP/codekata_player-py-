n=int(input())
l=[int(x) for x in input().split()]
if(n==len(l)):
  for i in range(0,n):
    for j in range(i+1,n):
      t=l[i]
      l[i]=l[j]
      l[j]=t
      break

print(*l)
