m=int(input())
l=[]
f=1
s=1
for i in range(m):
    l.append(list(map(int,input().split())))

for i in range(m):
    f=f*l[i][i]
    
for j in range(m):
    s=s*l[j][m-j-1]
    
print(s+f)
