def nonrepeat(n):
  l=[]
  v=''
  for i in n:
    if(i!=' '):
      if(n.count(i)==1):
        v+=i
  nr=' '.join(v)
  return nr

st=input()
print(nonrepeat(st))    
