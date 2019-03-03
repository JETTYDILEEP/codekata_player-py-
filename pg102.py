class pg102:
  def func(n,l):
    c=0
    l.sort()
    if(n==len(l)):
      for i in range(0,n-1):
        c=c+max(l[i],l[i+1])
    return c+4   

n=int(input())
l=[int(x) for x in input().split()]
print(pg102.func(n,l))
