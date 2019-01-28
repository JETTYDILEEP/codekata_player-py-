n=int(input())
l=[]
for i in range(1,n+2):
  if(n%i== 0):
    if(i%2==0):
      l.append(i)

print(*l,sep=" ")
