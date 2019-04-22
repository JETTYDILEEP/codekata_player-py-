class pg147:
  def func(n):
    for i in range(0,len(n)):
      if(i!=0 and i!=len(n)-1):
        n[i]=n[i][::-1]
      
    print(*n,sep=' ')  
n=input().split(' ')
pg147.func(n)
