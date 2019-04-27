class pg166:
  def gcd(a):
    b=1
    for i in range(1,a+1):
      b=b*i
    return b
m,n=map(int,input().split())
a=min(m,n)
print(pg166.gcd(a))
