n=int(input())
l=[int(x) for x in input().split()]
t=0
if(n==len(l)):
  for i in range(0,n):
    for j in range(0,n):
      if((l[j]&l[i])>0 and i!=j ): 
        t.append(l[i]&l[j])
      elif(len(l)==1):
        t=l[0]
       

print(t)       
