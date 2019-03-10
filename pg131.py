class pg131:
  def func(n):
    g,c,t=[],0,0
    while(n>0):
        c=n%10
        n//=10
        g.append(c)
    g.reverse()  
    for i in g:
      if(i%2!=0):
        t=t+i

    if(t%2==0):
      print('E')
    else:
      print('O')            
        
n=int(input())
pg131.func(n)
