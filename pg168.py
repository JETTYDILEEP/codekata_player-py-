n=input()
b=''
for x in range(1,len(n)):
    if(n[x].isnumeric()):
        b=b+(n[x-1]*int(n[x]))
print(b)
        
