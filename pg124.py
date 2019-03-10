n=int(input())
l=[int(x) for x in input().split()]
s,c=0,0
if(len(l)==n):
  while(True):
    c+=1
    for i in l:
      if c%i==0:
        s+=1
        continue
      else:
        break
    if s==n:
      break
    s=0      

print(c)
