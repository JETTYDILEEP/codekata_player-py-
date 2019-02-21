m,n=map(int,input().split())
t=1
p=1
for i in range(n):
  t=m*t
  m=m-1
for j in range(1,n+1):
  p=j*p
print(int(t/p))



