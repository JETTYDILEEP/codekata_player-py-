n=int(input())
l1=input().split(' ')
l2=input().split(' ')
s=[]
for i in l1:
    if(i in l2):
        s.append(i)
s=' '.join(s)
print(s)
