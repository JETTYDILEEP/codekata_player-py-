class pg116:
  def func(n,l):
    tl,t=[],[]
    if(n==len(l)):
      for i in range(0,n):
        if((l.count(l[i])>1) and (l[i] not in t)):
          t.append(l[i])
        elif((l.count(l[i])==1) and (l[i] not in tl)):
          tl.append(l[i])
      tl.sort() 
      tl.reverse()  
      t.sort()
      t.reverse()
      for i in range(0,len(tl)):
        t.append(tl[i])
    #print(tl)
    print(*t,sep=' ')

n=int(input())
l=[int(x) for x in input().split()]
pg116.func(n,l)
