n=int(input())
l=[int(x) for x in input().split()]
t=l.count(l[0])
if(n==len(l)):
  for i in range(n):
    if(l.count(i)>t):
      t=l.count(i)
print(t)
