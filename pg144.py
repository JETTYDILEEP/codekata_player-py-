n=int(input())
l=[int(x) for x in input().split()]
if(len(l)==n):
  t=[]
  for i in range(n):
    if((l[i]%l[i-1])==0):
      t.append(l[i])    
    else:
      continue
  print(*t,sep=' ')
  
