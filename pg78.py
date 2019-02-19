class pg78:
  def fun(m,n,l1,l2):
    if(m==len(l1) and n==len(l2)):
      for i in range(0,n-1):
        l1.append(l2[i])
      l1.sort()
      print(*l1,sep=' ')


M,N=map(int,input().split())
L1=[int(x) for x in input().split()]
L2=[int(x) for x in input().split()]
pg78.fun(M,N,L1,L2)
