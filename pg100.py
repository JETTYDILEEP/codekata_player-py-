n=int(input())
dic={10:'A',11:'B',12:'C',13:'D',14:'E',15:'f'}
s,i,l=0,0,[]
while(n!=0):
	s=s+((n%10)*(2**i))
	i=i+1
	n=n//10
while(s!=0):
	q=s%16
	s=s//16
	l.append(q)
l.reverse()

for i in range(len(l)):
  if(l[i] in dic):
    print(dic[l[i]],end='')
  else:  
	  print(l[i],end="")
