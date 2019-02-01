sen=str(input())
sen=sen.split()
string=str(input())
c=0
for i in range(0,len(sen)):
  if(sen[i]==string):
   c=c+1

print(c)    
