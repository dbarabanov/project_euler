#Starting in the top left corner of a 22 grid, there are 6 routes (without backtracking) to the bottom right corner.
#
#How many routes are there through a 2020 grid?

n = 21 

grid = [[0]*n]*n
for i in range(n):
    grid[0][i] = 1
    grid[i][0] = 1

for i in range(1,n):
    for j in range(1,n):
        grid[i][j] = grid[i-1][j]+grid[i][j-1]
print grid[n-1][n-1]
#137846528820
