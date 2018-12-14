def is_anagram(str1, str2):
    a = list(str1)
    a.sort()
    b = list(str2)
    b.sort()

    if(a == b):
        return('1')
    else:
        return('0')

n=int(input())
l=[]
for i in range(n):
    l.append(input())
s='kabali'
c=0
for j in range(n):
    if(is_anagram(s,l[j]) == '1'):
        c=c+1
print(c)
