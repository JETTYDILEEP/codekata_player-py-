n=input()
k=""
for i in n:
    if i.isupper():
        k=k+i.lower()
    else:
        k=k+i.upper()
print(k)
