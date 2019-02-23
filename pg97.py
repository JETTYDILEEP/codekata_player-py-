m,n=map(int,input().split())
v=0
for i in range(m,n+1):
  if(i%2!=0):
    v=v+i
print(v)
