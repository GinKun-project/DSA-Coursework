def rotate_char(c, direction):
    
    if direction == 1:
        return chr((ord(c) - ord('a') + 1) % 26 + ord('a'))
    
    elif direction == 0:
        return chr((ord(c) - ord('a') - 1) % 26 + ord('a'))

def apply_shifts(s, shifts):
    
    s = list(s)
    
   
    for start, end, direction in shifts:
        for i in range(start, end + 1):
            s[i] = rotate_char(s[i], direction)
    
    
    return ''.join(s)


s = "hello"
shifts = [[0, 1, 1], [2, 3, 0], [0, 2, 1]]
result = apply_shifts(s, shifts)
print(result)  
