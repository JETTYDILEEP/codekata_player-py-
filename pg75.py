n=int(input())
l=[int(x) for x in input().split()]
c=0
if(n==len(l)):
  for i in range(0,n-1):
    for j in range(i+1,n):
         if l[i]<l[j]:
           c=c+1
print(c)
