a = [[1,2,3],
     [4,5,6],
     [7,8,9]]

def transpose(a):
    return [list(row) for row in zip(*a)]

print(transpose(a))

