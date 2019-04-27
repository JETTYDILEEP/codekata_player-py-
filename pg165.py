class pg165:
  def func(m,n,l):
    l.sort()
    for i in range(m):
      if(l[i]>n):
        print(l[i])
        break
m,n=map(int,input().split())
l=[int(x) for x in input().split()]
pg165.func(m,n,l)
