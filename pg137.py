n=int(input())
l=bin(n)
l=l.replace('b',"")
l=list(l)
l.reverse()
c=0
for i in range(0,len(l)):
  if(int(l[i])==1):
    break
  elif(int(l[i])==0):
   c=c+1

print(c+1) 
