class pg161:
  def func(n):
    l,l1,l2=[],[],[]
    for i in range(n):
      l.append(str(input()))
    for i in range(n):
      l1=list(l[i])
      for i in range(len(l1)):
        l2.append(l1[i])

    for i in range(len(l2)):
      if(l2.count(l2[i])>1):
        print('yes')
        break
    else:
      print('no')
  
n=int(input())
pg161.func(n)
