class position:
  def pg95(n,p,k):
    l=[]
    while(n!=0):
      t=n%10
      l.append(t)
      n=n//10
    l.reverse()
    p=p+k
    return(l[p-1])

n,p,k=map(int,input().split())
print(position.pg95(n,p,k))
