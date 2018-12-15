n,k=map(int,input().split())
l=[]
l=list(map(int,input().split()))
k=map(int,input().split())
for i in k:
  if i not in l:
    l.append(i)
print(n,len(l))
