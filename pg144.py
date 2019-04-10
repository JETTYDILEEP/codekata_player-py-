n=int(input())
l=[int(x) for x in input().split()]
if(len(l)==n):
  for i in range(n):
    if((l[i]%l[i-1])==0):
      print(l[i],end=' ')    
    else:
      continue
  
