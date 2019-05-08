import string
m=input()
f=all(c in string.hexdigits for c in m)
if(f):
    print('yes')
else:
    print('no')
