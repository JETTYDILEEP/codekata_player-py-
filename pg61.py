N,X=map(int,input().split())
c=0
l=[int(x) for x in input().split()]
if(N==len(l)):
  for i in range(0,N):
    for j in range(0,N):
      if(i!=j and l[i]+l[j]==X):
        c=c+1
      else:
        continue

if(c>0):
  print('yes')
else:
  print('no')  
