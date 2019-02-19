n=int(input())
l=[int(x) for x in input().split()]
tl=[]
t=0
if(n==len(l)):
  for i in range(0,n):
    for j in range(0,n):
      t=abs(l[j]-l[i])
      tl.append(t)
      t=0
  print(max(tl))  
