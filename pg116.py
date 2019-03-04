class pg116:
  def func(n,l):
    tl,t=[],[]
    if(n==len(l)):
      for i in range(0,n):
        if(l[i] not in tl):
          tl.append(l[i])
    for i in range(0,len(tl)):
      if(l.count(tl[i])>1):
        t.append(tl[i])

    t.sort()
    t.reverse()
    for i in range(0,len(tl)):
      if(tl[i] not in t):
        t.append(tl[i])

    print(*t,sep=' ')

n=int(input())
l=[int(x) for x in input().split()]
pg116.func(n,l)
