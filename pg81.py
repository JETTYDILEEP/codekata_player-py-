n=int(input())
l=[int(x) for x in input().split()]
t=[]
if(n==len(l)):
  for i in range(0,n):
    for j in range(0,n):
      if((l[j]&l[i])== l[i]):
        t.append(l[i])

print(max(t))       
