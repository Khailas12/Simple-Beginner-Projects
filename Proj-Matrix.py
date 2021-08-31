x = [[1, 2, 3], 
    [4, 5, 6],
    [7, 8, 9]]

y = [[10, 11, 12],
    [13, 14, 15],
    [16, 17, 18]]

res = [[0, 0, 0], 
        [0, 0, 0],
        [0, 0, 0]]

def function():
    for i in range(len(x)):
        for j in range(len(y[1])):
            res[i][j] = x[i][j] + y[i][j]
    
    for r in res:
        print(r)
function()



