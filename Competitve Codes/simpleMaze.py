X = [0,0,-1,1]
Y = [-1,1,0,0]

def outOfMaze(x, limit):
    return (x < 0 or x == limit)

def traverseMaze(maze, x, y, visited):
    
    visited[x][y] = True
    
    for k in range(4):
        if outOfMaze(x+X[k], len(maze)) or outOfMaze(y+Y[k], len(maze[x])):
            return True
        
        elif maze[x+X[k]][y+Y[k]] != '#' and visited[x+X[k]][y+Y[k]] == False:
            if traverseMaze(maze, x+X[k], y+Y[k], visited):
                
                visited[x][y] = True
                return True
    
    visited[x][y] = False
    return False
        
def has_exit(maze):
    
    visited = []
    for i in range(len(maze)):
        visited.append([False]*len(maze[i]))
    
    kateCount = 0
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 'k':
                x, y = i, j
                kateCount+=1
            
    if kateCount == 1:
        return traverseMaze(maze, x, y, visited)
    
    raise Exception("There should no be multiple Kates")
    
if __name__ == '__main__':
    maze = ["k ",
        "kk"]
    
    print (has_exit(maze))