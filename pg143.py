n=int(input())
l1=[int(x) for x in input().split()]
l2=[int(x) for x in input().split()]
if(len(l1)==len(l2) and len(l1)==n):
  for i in range(n):
    for j in range(n):
      if(l2[i]<l2[j]):
        l2[i],l2[j]=l2[j],l2[i]
        l1[i],l1[j]=l1[j],l1[i]  
        

  print(*l1,sep=' ')
