class pg115:
  def func(s,m):
    s=list(s)
    m=list(m)
    if(len(s)>1):
      #s[len(s)-1]=m[0]
      for i in range(0,len(m)):
        s.append(m[i])

      print(*s,sep='')
    else:
      for i in range(0,len(m)):
        s.append(m[i])
      print(*s,sep='')

s,m=map(str,input().split())
pg115.func(s,m)
