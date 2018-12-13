m,n = map(int,input().split())
z=max(m,n)
x=z
y = min(m,n)
while(x%y!=0):
  x+=z
print(x)    
