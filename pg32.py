def func(s,v):
  l=[int(x) for x in input().split()]
  if(s==len(l)):
      if v in l:
        return 'Yes'
      else:
        return 'No' 
  else:
    print('invalid list')
  
m,n=map(int,input().split())
print(func(m,n))
