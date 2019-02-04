n=int(input())
l1=[int(x) for x in input().split()]
l2=[int(x) for x in input().split()]
s=[]
if(len(l1)==n and len(l2)==n):
  for i in l2:
    if(i in l1):
        s.append(i)


print(*s,sep=' ')
