n=input()
v=""
for i in n:
    if(i==" " or n.count(i)==1):
        v=v+i
    else:
        v=v+i.upper()
print(v)
