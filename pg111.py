class pg111:
  def func(m,n,l):
    l1,l2,l3=[],[],[]
    if((m+n)==len(l)):
      for i in range(m):
        l1.append(l[i])
      #print(l1)
      
      for i in range(m,m+n):
        l2.append(l[i])
      
      #print(l2)
      for i in range(n):
        if(l2[i] in l1):
          l3.append(l2[i])

      print(*l3,sep=' ')  

m,n=map(int,input().split())
l=[int(x) for x in input().split()]
pg111.func(m,n,l)
