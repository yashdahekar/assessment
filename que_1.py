'''Write an efficient algorithm that searches for a value target in an m x n integer m. This m has the following properties:

Integers in each row are sorted from right to left.

The first integer of each row is greater than the last integer of the previous row.'''


def search_matrix(m, t):
    if not m or not m[0]:
        return False
    
    rows = len(m)
    cols = len(m[0])

    row = 0
    col = cols - 1
    
    while row < rows and col >= 0:
        if m[row][col] == t:
            return True
        elif m[row][col] < t:
            row += 1  #Moves down if the value is less than target
        else:
            col -= 1  #Moves left if the value is less than target greater than target
    
    return False

# Example:
m = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
t = 3
print(search_matrix(m, t))  
