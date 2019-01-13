def func(n):
  l=list(n) 
  c1=0
  c2=0
  for i in range(len(l)):
    if(l[i]=='('):
      c1=c1+1
    elif(l[i]==')'):
      c2=c2+1

  if(c1==c2):
    return "yes"
  else:
    return "no" 

s=str(input())
print(func(s))
