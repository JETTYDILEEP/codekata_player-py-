class pg164:
  def binarySearch(arr, l, r, x):   
      if r >= l: 
        mid = l + (r - l)/2
        mid=int(mid)
        if arr[mid] == x: 
          return mid 
        elif arr[mid] > x: 
          return pg164.binarySearch(arr, l, mid-1, x) 
        else: 
          return pg164.binarySearch(arr, mid + 1, r, x) 
    
      else: 
        return -1
    
n,x=map(int,input().split())
arr=[int(x) for x in input().split()]
  

result = pg164.binarySearch(arr, 0, n-1, x) 
  
if result != -1: 
    print(x)

else: 
    for i in range(n):
      if(arr[i]<x):
        print(arr[i])
        break
