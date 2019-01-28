def rightRotate(lists, num): 
    output_list = [] 
      
    for item in range(len(lists) - num, len(lists)): 
        output_list.append(lists[item]) 
      
         
    for item in range(0, len(lists) - num):  
        output_list.append(lists[item]) 
          
    return ''.join(output_list)
  
 
s,times=input().split()
rotate_num=int(times)
list_1=list(s)
  
print(rightRotate(list_1, rotate_num)) 

