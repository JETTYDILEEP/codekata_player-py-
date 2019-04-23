s,k=input().split()
s=list(s)
l=[]
o=""
for i in range(int(k)-1,len(s),int(k)):
  l.append(i)
for i in range(len(s)):
  if i in l:
    o+=s[i].upper()
  else:
    o+=s[i]
print(o)
