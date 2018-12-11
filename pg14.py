s=int(input())
string=input()
n=len(string)
t=''
v=['a','e','i','o','u','A','E','I','O','U']
if(s==n):
  for i in range(n):
	  if string[i] in v:
		  continue
	  t+=string[i]
str = "" 
for i in t: 
   str = i + str
print(str)

