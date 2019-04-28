n=input().split(' ')
for j in range(len(n)):
    n[j]=''.join(sorted(n[j]))
print(*n,sep=' ')
