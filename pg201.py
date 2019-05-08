def catalan(n): 
   
    if n <= 2 : 
        return 1 
  
    # Catalan(n) is the sum of catalan(i)*catalan(n-i-1) 
    res = 0 
    for i in range(n): 
        res += catalan(i) * catalan(n-i-1) 
  
    return res 
  
m=int(input()) 
for i in range(0,m+1): 
    print(catalan(i),end=' ') 
