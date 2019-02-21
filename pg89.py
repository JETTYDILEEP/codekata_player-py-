class pg89:
  def permutation(m,n):
    t=1
    for i in range(n):
      t=m*t
      m=m-1
    return t

m,n=map(int,input().split())
print(pg89.permutation(m,n))




