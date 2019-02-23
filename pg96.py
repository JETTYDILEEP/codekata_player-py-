class sumoffl:
  def pg96(n):
    l=[]
    while(n!=0):
      t=n%10
      l.append(t)
      n=n//10
    l.reverse()
    p=l[0]+l[len(l)-1]
    return(p)

n=int(input())
print(sumoffl.pg96(n))
