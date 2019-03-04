class pg108:
  def func(n,l):
    s=[]
    if(n==len(l)):
      c=0
      for i in range(n):
        c=c+l[i]
        s.append(c)

    print(*s,sep=' ')

n=int(input())
l=[int(x) for x in input().split()]
pg108.func(n,l)
