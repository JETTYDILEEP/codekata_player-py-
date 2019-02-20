n=int(input())
l=[int(x) for x in input().split()]
t=[]
if(n==len(l)):
  for i in range(0,n):
    for j in range(0,n):
      if((l[j]|l[i])>0):
        t.append(l[i]|l[j])

print(max(t))       
