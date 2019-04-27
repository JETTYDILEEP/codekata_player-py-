class pg162:
  def func(n,m):
    l,l1,l2=[],[],[]
    for i in range(n):
      l.append(str(input()))
    for i in range(n):
      l1=list(l[i])
      for i in range(len(l1)):
        l2.append(l1[i])

    for i in range(len(l2)):
      if(l2.count(l2[i])>=m):
        print('yes')
        break
    else:
      print('no')
  
n,m=map(int,input().split())
pg162.func(n,m)
