class pg146:
  def func(m,n):
    t1,t2=1,1
    for i in range(1,m+1):
     t1=t1*i
    for j in range(1,n+1):
      t2=t2*j 


    print(int(t1/t2))

m,n=map(int,input().split())
pg146.func(m,n)
