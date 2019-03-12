class pg135:
  def func(n,l):
    t,g=[],[]
    if(len(l)==n):
      for i in range(0,int(n/2)):
        t.append(l[i])
      t.sort()
      for i in range(int(n/2),n):
        g.append(l[i])
      g.sort()
      g.reverse()
      for i in g:
        t.append(i)
      print(*t,sep=' ')
n=int(input())
l=[int(x) for x in input().split()]
pg135.func(n,l)
