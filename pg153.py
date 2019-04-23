s,k=map(str,input().split())
k=int(k)
k-=1
ans=s[k::k+1]
print(*ans,sep=' ')
