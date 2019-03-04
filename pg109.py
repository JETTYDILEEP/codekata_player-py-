class pg109:
  def func(n,l):
    s=[]
    
    if(n==len(l)):
      c=0
      for i in range(1,n+1):
        c=c+l[n-i]
        s.append(c)
    s.reverse()
    print(*s,sep=' ')

n=int(input())
l=[int(x) for x in input().split()]
pg109.func(n,l)
