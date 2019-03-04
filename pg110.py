class pg110:
  def func(n,l):
    s=[]
    t=[]
    c=0
    te=0
    if(n==len(l)):
      
      for i in range(1,n+1):
        c=c+l[n-i]
        t.append(c)
      for j in range(1,n+1):
        te=te+l[n-j]
        s.append(te)
      s.reverse()
      for i in range(n):
        s[i]=s[i]+t[i]
    
      print(*s,sep=' ')

n=int(input())
l=[int(x) for x in input().split()]
pg110.func(n,l)
