def smal(N,K):
  arr=[int(x) for x in input().split()]
  if(len(arr)==N):
    print(arr[K-1])

N,K=map(int,input().split())
smal(N,K)
