n=int(input())
c=0
for i in range(1,n+2):
  c=n/i
  if(c%2!=0 and n%i==0):
      print(i)
      break
