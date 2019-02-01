def fun1(n):
  for i in range(1,n+1):
    fun2(i,n)

def fun2(i,n):
  if(i!=n):
    if(n%i==0 and i%2!=0):
      print(i,end=' ')
  else:
    print(i,end='')    

n=int(input())
fun1(n)
