class check:
  def pg98(n,m):
    l=[]
    c=0
    while(n!=0):
      t=n%10
      l.append(t)
      n=n//10

    for i in range(0,m):
      if(i in l):
        c=c+1
    if(c==m):
      return 'yes'
    else:
      return 'no'

n,m=map(int,input().split())
print(check.pg98(n,m))
