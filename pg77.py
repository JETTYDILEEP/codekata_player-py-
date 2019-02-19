n=int(input())
l=[int(x) for x in input().split()]
c=1
if(n==len(l)):
  for i in range(0,n-1):
    if(l[i]+1==l[i+1]):
      c=c+1
    else:
      break


if(c>1):
  print(c)
else:
  print(c-1)
