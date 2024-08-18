def optimize_boarding(head, k):
    n = len(head) 
    result = [] 

   
    for i in range(0, n, k):
        
        chunk = head[i:i+k]
       
        result.extend(reversed(chunk))
    
    return result


head1 = [1, 2, 3, 4, 5]
k1 = 2
print(optimize_boarding(head1, k1)) 


head2 = [1, 2, 3, 4, 5]
k2 = 3
print(optimize_boarding(head2, k2)) 

