def powk(m,n):
  for i in range(m+1): 
    if(n**i==m):
      print('yes')
      break
    
  else:
    print('no')  

m,n=map(int,input().split())
powk(m,n)
