
newGrid=[[],[],[],[],[],[],[],[],[]]

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

print (grid)

for i in range (len(grid[0])):          #get new number of rows
        for j in range (len(grid)):     #new number of columns
            print(grid[j][i],end='')    #flip i and j index. End stops printing to new line each time
        print ()



#lists=len(grid)
#while lists >0:
#    for i in range(len(grid)):
#        for j in range(len(grid[i])):
#            newGrid.insert(0,grid[i][j])
#            del grid[i][j]
#            print(newGrid, end='')
#        print()
    
#    lists-=lists
    
    #for index in grid[0:10]:
    #    for character in grid[lists]:
    #   newGrid.insert(0,grid[character])
    #   print(newGrid, end='')

