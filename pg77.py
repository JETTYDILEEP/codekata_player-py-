class incarr:
  def fun(n,l):
    c=1
    l1=[]
    if(n==len(l)):
      for i in range(0,n-1):
        if(l[i]+1==l[i+1]):
          c=c+1
        else:
          l1.append(c)
          c=1
      l1.append(c)
    print(max(l1))

N=int(input())
L=[int(x) for x in input().split()]
incarr.fun(N,L)
