m=int(input())
list=[]
for i in range(m):
    list.append(input())
min=len(list[0])
pos=0
for i in range(m):
    if min>len(list[i]):
        min=len(list[i])
        pos=i
    
print(list[pos])
