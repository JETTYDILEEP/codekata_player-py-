import random
class pg103:
    def func(n,l):
      c=0
      random.shuffle(l)
      if(n==len(l)):
        for i in range(0,n-1):
          c=c+max(l[i],l[i+1])

      return c  

n=int(input())
l=[int(x) for x in input().split()]
print(pg103.func(n,l))
