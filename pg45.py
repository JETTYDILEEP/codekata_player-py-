def perimeter(p,a):

  per=int(p/2)
  are=int(a**0.5)
  if(per*2==p and are*are==a):
   print('yes')
  else:
    print('no') 

p,a=map(int,input().split())
perimeter(p,a)
