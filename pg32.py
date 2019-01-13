def func(s,v):
  l=[int(x) for x in input().split()]
  if(s==len(l)):
      if v in l:
        return 'yes'
      else:
        return 'no' 
  else:
    print('invalid list')
  
m,n=map(int,input().split())
print(func(m,n))
