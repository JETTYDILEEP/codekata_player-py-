class pg163:
  def binarySearch(arr, l, r, x):   
      if r >= l: 
        mid = l + (r - l)/2
        mid=int(mid)
        if arr[mid] == x: 
          return mid 
        elif arr[mid] > x: 
          return pg163.binarySearch(arr, l, mid-1, x) 
        else: 
          return pg163.binarySearch(arr, mid + 1, r, x) 
    
      else: 
        return -1
    
n,x=map(int,input().split())
arr=[int(x) for x in input().split()]
  

result = pg163.binarySearch(arr, 0, n-1, x) 
  
if result != -1: 
    print ("yes")
else: 
    print ("no")
