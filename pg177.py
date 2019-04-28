n=input().split(' ')
for i in range(len(n)):
    n[i]=''.join(sorted(n[i]))
print(*n,sep=' ')
