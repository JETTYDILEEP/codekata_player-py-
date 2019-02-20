n=int(input())
a=[int(x) for x in input().split()]
if(n==len(a)):
  s=a[0] 
  for i in range(1,n):
    s=s|a[i]
  print(s)
