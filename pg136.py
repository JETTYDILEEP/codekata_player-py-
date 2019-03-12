class pg136:
  def func(m,n,l):
    if(m==len(l)):
      c=l.count(n)
      if(c>=1):
        print('yes',c)
      else:
        print('no')

m,n=map(int,input().split())
l=[int(x) for x in input().split()]
pg136.func(m,n,l)
