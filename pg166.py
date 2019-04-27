class pg166:
  def gcd(a,b):
    if(b==0):
      return a
    else:
      return pg166.gcd(b,a%b)
  
m,n=map(int,input().split())
a,b=1,1
for i in range(1,m+1):
  a=a*i
for i in range(1,n+1):
  b=b*i
print(pg166.gcd(a,b))
