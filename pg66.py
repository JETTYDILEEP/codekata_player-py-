class program:  
  def fun(N,K):
    l=[int(x) for x in input().split()]
    t=0
    if(N==len(l)):
      for i in l:
        if(l.count(i)==K):
          t=i
    print(t)  

  n,k=map(int,input().split())
  fun(n,k)
