class pg129:
  def func(n,l):
    c=0
    if(n==len(l)):
      for i in range(0,n):
        c=l[i]-c
      
      print(c)

n=int(input())
l=[int(x) for x in input().split()]
pg129.func(n,l)
