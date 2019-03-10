class pg126:
  def func(n,m,l):
    g=[]
    if(len(l)==n):
      for i in l:
        c=l.count(i)
        if(c<m):
          g.append(i)
    g.sort()
    print(*g,sep=' ')

n,m=map(int,input().split())
l=[int(x) for x in input().split()]
pg126.func(n,m,l)
