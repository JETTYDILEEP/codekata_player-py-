n=int(input())
l=[int(x) for x in input().split()]
m=max(l)
c=0
g=[]
if(n==len(l)):
  for i in range(1,m+1):
      c=0
      for j in l:
          if j%i==0:
              c+=1
      if c==len(l):
          g.append(i)
  s=max(g)
  print(s)
