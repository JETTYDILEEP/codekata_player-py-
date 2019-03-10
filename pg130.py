class pg130:
  def func(n,l):
    c,g=0,[]
    if(n==len(l)):
      for i in l:
        c=i+c       
        g.append(c)
      print(*g,sep=' ')

n=int(input())
l=[int(x) for x in input().split()]
pg130.func(n,l)
