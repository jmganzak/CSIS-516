

Page
1
of 4
global direction
show_path = True #show path variable
global pathVisited
pathVisited = [] #holds everywhere user has walked
#read file
with open('init_grid.txt', 'r') as f:
    rows, cols = [int(item)for item in f.readline().split()]
    grid = [['.' for x in range(cols)] for x in range(rows)] #reading file to get 
initial direction, positiion, grid, and number of rows and colums
    pacman_row, pacman_col = [int(item)for item in f.readline().split()]
    pacman_dir = f.readline().strip()
    
    #update pacmans direction
    if pacman_dir == 'N':
        grid[pacman_row][pacman_col] = '^'
    elif pacman_dir == 'E':
        grid[pacman_row][pacman_col] = '>'
    elif pacman_dir == 'S':
        grid[pacman_row][pacman_col] = 'v'
    elif pacman_dir == 'W':
        grid[pacman_row][pacman_col] = '<'
    num_obstacles = int(f.readline().strip()) #grab number of obstacles
    for _ in range(num_obstacles):
        row, col = [int(item)for item in f.readline().split()] #add obstacles to 
grid
        grid[row][col] = 'x'
    
    items = []
    num_items = int(f.readline().strip()) #grab number of items on the grid
    for _ in range(num_items):# Update the grid to reflect the position of each 
item
        row, col = [int(item)for item in f.readline().split()]
        grid[row][col] = 'o'
        items.append([int(item) for item in f.readline().split()])
#Printing grid function
def printGrid(grid, show_path):
    for row in grid:
        for symbol in row:
            if symbol == '.' and show_path==True: #check the symbol and if 
show_path is true
                print('.', end=' ')
            else:
                print(symbol, end=' ')
        print()
def Hide(pathVisited,show_path): #this function is for hiding/showing the path
    if show_path==False:
        for i,j in pathVisited:
           if [i,j] == [pacman_row,pacman_col]:
            grid[i][j] = " "
    else:
        pass
    return grid
def movePac(grid, pac_dir, pac_row, pac_col, x): #Moving pacman function, depending
on direction
    if pac_dir=="N":
        pos = -1,0
    elif pac_dir=="S":
        pos = 1,0
    elif pac_dir=="E":
        pos = 0,1
    elif pac_dir=="W":
        pos = 0,-1
    newRow,newCol = pac_row,pac_col
    temp = False
    finalRow = pos[0]*x+pac_row
    finalCol = pos[1]*x+pac_col
    for i in range(x): #add position to new row/col
        newRow += pos[0]
        newCol += pos[1]
        if finalRow < 0 or finalRow >= len(grid) or finalCol < 0 or finalCol >= 
len(grid[0]): #Check if pacman goes out of grid
            #print(f'Out of bounds at: {newRow}, {newCol}')
            print("Invalid Move")
            temp = True
            return pac_row,pac_col,[]
        elif grid[newRow][newCol] == 'x': #Check if pacman hit a wall
            #print(f'Pacman hit a wall at: {newRow},{newCol}') 
            print('Invalid Move')
            temp = True
            return pac_row,pac_col,[]
        
    if temp == False:
        pathVisited = [[pos[0]*i+pac_row,pos[1]*i+pac_col] for i in range(x)]
    return newRow,newCol,pathVisited
    
 
def updateGrid(grid, pacman_position, pacman_direction,pathVisited): #update pacman
position when moving
    row, col = pacman_position
     #update direction
    grid[row][col] = pacman_direction 
    if show_path == True:
        for i,j in pathVisited:
         if [i,j] != [row,col] and [i,j] != "@" or [i,j] != "o": #check symbol
                grid[i][j] = " "
    else:
       for i,j in pathVisited:
         if [i,j] != [row,col] and [i,j] != "@" or [i,j] != "o": #check symbol 
                grid[i][j] = "." 
    if  grid[row][col] == "o":
        grid[row][col] = "@"
        items.append(grid[row][col]) #Add to items array of current position
    elif grid[row][col] == "@":
        items.append(grid[row][col])    
    return grid
    
printGrid(grid, show_path)#print grid
print("-----Welcome to Pacman-----")
print("L:   Turn Left")
print("R:   Turn Right")
print("[x]:   Move x number of steps") #main menu text
print("C:   Consume Item")
print("P:   Place Item")
print("S:   Show/Hide Path")
print("Q:   Quit")
while True: #commands for navigating
    print()
    
    command = input('Enter command: ')
    if command == "Q" or command == "q":  #exit on q
        #print('Exiting Program')
        exit()
    if command == 'C' or command == 'c': #Consume command
        if grid[pacman_row][pacman_col] == "@":
            if show_path == True:
                grid[pacman_row][pacman_col] = direction
        else:
            print('No item to consume')        
    if command == 'P' or command == 'p': #place command
        if [pacman_row,pacman_col] not in items:
            items.append([pacman_row,pacman_col])
            pacman_direction=pacman_dir
            pacman_position = pacman_row,pacman_col
            updateGrid(grid, pacman_position, pacman_direction,pathVisited)
            grid[pacman_row][pacman_col] = "@"
    if command == "s" or command =="S": #show path
        if show_path == True:
            show_path = False
            grid = Hide(show_path,pathVisited)
            print(f'Show path is set to: {show_path}') #show path results
        elif show_path == False:
            show_path = True
            print(f'Show path is set to: {show_path}')
        
    if command == 'L' or command == "l": #turn pacman left depending on direction
        print("Grid Looks Like: ")
        if pacman_dir == 'N':
            pacman_dir = 'W'
            grid[pacman_row][pacman_col] = '<'
            direction = '<'
        elif pacman_dir == 'E':
            pacman_dir = 'N'
            grid[pacman_row][pacman_col] = '^'
            direction = '^'
        elif pacman_dir == 'S':
            pacman_dir = 'E'
            grid[pacman_row][pacman_col] = '>'
            direction =  '>'
        elif pacman_dir == 'W':
            pacman_dir = 'S'
            grid[pacman_row][pacman_col] = 'v'
            direction =  'v'
            
    elif command == 'R' or command == 'r': #turn pacman right depending on  current
direction
        print("Grid Looks Like: ")
        if pacman_dir == 'N':
            pacman_dir = 'E'
            grid[pacman_row][pacman_col] = '>'
            direction = '>'
        elif pacman_dir == 'E':
            pacman_dir = 'S'
            grid[pacman_row][pacman_col] = 'v'
            direction = 'v'
        elif pacman_dir == 'S':
            pacman_dir = 'W'
            grid[pacman_row][pacman_col] = '<'
            direction =  '<'
        elif pacman_dir == 'W':
            pacman_dir = 'N'
            grid[pacman_row][pacman_col] = '^'
            direction =  '^'
    elif command.isnumeric(): #check is user given command is number for moving
        if pacman_dir == 'N':
            direction = '^'
        elif pacman_dir == 'E':
            direction = '>'
        elif pacman_dir == 'S':
            direction =  'v'
        elif pacman_dir == 'W':
            direction =  '<'
        pacman_row,pacman_col,pathVisited = 
movePac(grid,pacman_dir,pacman_row,pacman_col,int(command))
        pacman_position = pacman_row,pacman_col
        pacman_direction=pacman_dir
        print("Grid Looks Like: ") # update grid after pacman moves
        grid = updateGrid(grid,pacman_position,direction,pathVisited)
    else:
        print('Invalid input')   
    printGrid(grid,show_path)
#
