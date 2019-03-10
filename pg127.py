class pg127:
  def func(n,m):
    g=[]
    for i in range(0,len(n)):
      if(n[i]==m):
        continue
      else:
        g.append(n[i])     
    
    print(*g,sep=' ')

n=str(input()).split()
m=str(input())
pg127.func(n,m)
