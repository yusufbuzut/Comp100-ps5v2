def print_paths(grid):
    '''
    Print all of the paths starting from the top-left cell and ending in the bottom-right cell such that the path is strictly increasing.

    grid (list of lists): The grid that we are moving on. It is a matrix in the form of list of lists. the element in the i'th row and j'th column is accesible by grid[i][j] (indexing is 0 based)

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Example:
    >>> print_paths([[1,4,3],[5,6,7]])
    [1, 4, 6, 7]
    [1, 5, 6, 7]

    Note: depending on your implementation, you may print the permutations in
    a different order than what is listed here.
    You must not return anything. You should only print the paths.
    '''
    def printpath2(grid, i, j, m, n, path, pi):
        if (i == m - 1):
            for k in range(j, n):
                path[pi + k - j] = grid[i][k]
            z=[]
            for l in range(pi + n - j):

                z.append(path[l])
            print(z)

            return 

        if (j == n - 1):

            for k in range(i, m):
                path[pi + k - i] = grid[k][j]
            z = []
            for l in range(pi + m - i):
                z.append(path[l])
            print(z)
            return

        path[pi] = grid[i][j]
        if grid[i][j]<grid[i+1][j]:
            printpath2(grid, i + 1, j, m, n, path, pi +1)
        if grid[i][j]<grid[i][j+1]:
            printpath2(grid, i, j + 1, m, n, path, pi + 1)


    path = [0 for i in range(len(grid) + len(grid[0]))]


    printpath2(grid, 0, 0, len(grid), len(grid[0]), path, 0)
      
    


    
    
    