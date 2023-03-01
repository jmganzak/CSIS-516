file = input('Enter file name: ')
print("Finished Reading File.")
print()
userfile=open(file, 'r') 
people = userfile.readline() #Grab file, read it in
people = int(people)
net = [[] for _ in range(people)] #network of friends
def start():#Error checking to ensure inputs are correct
    temp =(input(f'Enter user id in the range 0 to {people -1} (-1 to quit) : '))
    if temp.isnumeric(): #check if numeric
        if int(temp)<people: #check if number is in range
            return int(temp)
        else:
            print(f'Error: input must be an int between 0 and {people}')
            return start()
    elif temp=="-1": #quit
        print("Goodbye!")
        exit()
    else: #check for letters
        print(f'Error: input must be an int between 0 and {people}')
        return start()
def popAdjMat(file):
    with open(file,'r') as f: #Grabs all strings from file and return adjMat
        num = int(f.readline().strip()) #Read file and strip
        adjMat = [[0 for x in range(num)] for y in range(num)]
        for line in f: #Grab file/user connection and friend
            data = [int(x) for x in line.strip().split()] 
            adjMat[data[0]][data[1]] = 1
            adjMat[data[1]][data[0]] = 1
        return adjMat
def rec_friend(adjMat, user):
    friend = [] #make array for friend
    for x in range(len(adjMat)): 
        if adjMat[user][x] == 1:
            friend.append(x)
    rec_friend = -1
    maxFriend = -1
    commonFriend=0
    for x in range(len(adjMat)): #Find commonFriend and return rec_Friend with the 
most in common
        if x != user and adjMat[user][x] == 0: #Check if common connection, or keep
at 0. If common friend, add 1
            commonFriend = 0
            for y in friend:
                if adjMat[x][y] == 1:
                    commonFriend +=1 #connection
        if commonFriend > maxFriend:
            rec_friend = x
            maxFriend = commonFriend
    return rec_friend
def network(adjMat): #check size of network
    if len(adjMat) > 10:
        print('**Network representation too large to show**')
    else:
        print("Network shown below:") #call network diagram
        showNet(userfile)
def showNet(userFile): #Show network diagram of file
    for line in userFile: #Check each line
        x,y = line.strip().split(" ") 
        x = int(x)
        y = int(y)
        if net[x].count(y) == 0:
            net[x].append(y)        
        if net[y].count(x) == 0:
            net[y].append(x)
    for i in range(people):
        print(i, " :", net[i])
adjMat = popAdjMat(file) 
network(adjMat)
print()
user = start()
print(f'The suggested friend for {user} is {rec_friend(adjMat, user)}') 
#       
