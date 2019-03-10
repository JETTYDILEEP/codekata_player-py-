class pg128:
  def func(n,l):
    c=1
    if(n==len(l)):
      for i in range(0,n):
        c=c*l[i]
      
      if(c%2==0):
        print('even')
      else:
        print('odd') 
    

n=int(input())
l=[int(x) for x in input().split()]
pg128.func(n,l)
