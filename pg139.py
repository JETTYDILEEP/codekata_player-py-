class pg139:
  def func(n):
    l=bin(n)
    l=l.replace('b',"")
    l=list(l)
    c=0
    for i in range(0,len(l)):
      if(int(l[i])==1):
        c=c+1
      
    return c
n=int(input())
print(pg139.func(n))
