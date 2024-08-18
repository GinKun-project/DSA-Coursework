def most_utilized_class(n, classes):
    
    classes.sort(key=lambda x: (x[0], -x[2]))
    
   
    room_end_time = [0] * n  
    room_count = [0] * n     
    
    
    for start, end, students in classes:
       
        earliest_room = 0
        for i in range(1, n):
            if room_end_time[i] < room_end_time[earliest_room]:
                earliest_room = i
        
        if room_end_time[earliest_room] <= start:
            room_end_time[earliest_room] = end
        else:
            
            room_end_time[earliest_room] += (end - start)
        
      
        room_count[earliest_room] += 1
    
    
    max_classes = max(room_count)
    for i in range(n):
        if room_count[i] == max_classes:
            return i


n1 = 2
classes1 = [[0, 10, 30], [1, 5, 25], [2, 7, 20], [3, 4, 10]]
print(most_utilized_class(n1, classes1))  # Output: 0

n2 = 3
classes2 = [[1, 20, 30], [2, 10, 25], [3, 5, 20], [4, 9, 15], [6, 8, 10]]
print(most_utilized_class(n2, classes2))  # Output: 1


