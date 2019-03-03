class pg106:
  def func(n,l):
    d=[]
    for i in range(n):
      if(l[i] not in d):
        d.append(l[i])
    print(*d,sep=' ')

n=int(input())
l=[int(x) for x in input().split()]
pg106.func(n,l)
