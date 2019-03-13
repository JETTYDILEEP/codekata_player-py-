class pg140:
  def func(n):
    c=0
    for i in n:
      if(i=='a' or i=='b'):
        c=c+1

    if(c==len(n)):
      print('yes')
    else:
      print('no')   
    
      
   
n=str(input())
pg140.func(n)
