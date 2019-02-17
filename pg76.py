class eveodd:
  def ope(A,l):
    c=0
    if(A==len(l)):
      for i in range(0,A):
        if l[i]%2==0:
            c=c+1
            d=l[i]
        else:
          di=l[i]
    if c==1:
        print(d)
    else:
        print(di)

A=int(input())
l=[int(x) for x in input().split()]
eveodd.ope(A,l)        
