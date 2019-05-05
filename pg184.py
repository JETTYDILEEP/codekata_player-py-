def arraySum (arr, n) : 
  
    sm = 0
    i = 0
  
    while(i<n) : 
        sm = sm + arr[i] 
        i = i + 1
    return sm 
  

def smallest (arr, n) : 
  
    small = 1000000000
  
    for i in range(0, n) : 
  
        if (arr[i] < small) : 
            small = arr[i] 
    return small 
      
  

def minOp (arr, n) : 
      
     
    sm = arraySum (arr, n) 
  
    
    small = smallest (arr, n) 
  
    
    minOperation = sm - (n * small) 
  
    
    return minOperation-1 
      

n =int(input()) 
arr = [int(x) for x in input().split()] 
print(  minOp (arr, n)) 
