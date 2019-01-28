def leftrotate(arr,d,n):
  for i in range(d):
    operation(arr,n)

def operation(arr,n):
  temp=arr[0]
  for i in range(n-1):
    arr[i]=arr[i+1]
  arr[n-1]=temp

def printarray(arr,n):
  for i in range(n):
    print("%s"%a[i],end='')



s,times=input().split()
times=int(times)
a=list(s)
size=len(s)

leftrotate(a,times,size)
printarray(a,size)
