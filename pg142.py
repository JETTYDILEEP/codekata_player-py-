n,m=map(int,input().split())
l,c=[],0
for i in range(n):
  l.append(str(input()))
for i in range(n):
  for j in range(n):
    if(l[i]==l[j] and i!=j):
      c=c+1
      
if(c==m):
  print('yes')
else:
  print('no') 
