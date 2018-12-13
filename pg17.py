m,n = map(int,input().split())
x=max(m,n)
y = min(m,n)
while(x%y!=0):
  x+=x
print(x)    
