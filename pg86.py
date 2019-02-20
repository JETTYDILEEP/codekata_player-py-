n=int(input())
l=[int(x) for x in input().split()]
t=0
if(n==len(l)):
  for i in range(0,n):
    for j in range(i+1,n):
      t=l[i]^l[j]

print(t)       
