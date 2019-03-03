class pg104:
    def func(n,l):
      c=0
      if(n==len(l)):
        for i in range(0,n):
          if(i!=n-1):
            c=c+(l[i]+l[i+1])
          else:
            c=c+0
      return c  

n=int(input())
l=[int(x) for x in input().split()]
print(pg104.func(n,l))
