# -----------
# User Instructions:
# 
# Modify the function search so that it returns
# a table of values called expand. This table
# will keep track of which step each node was
# expanded.
#
# Make sure that the initial cell in the grid 
# you return has the value 0.
# ----------

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], #go down
         [ 0, 1]] #  # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    # ----------------------------------------
    # modify code below
    # ----------------------------------------
    closed = [[0] * len(grid[0]) for i in grid]
    closed[init[0]][init[1]] = 1
    expand = [[-1]*len(grid[0]) for i in grid]
    
    g=0
    x=init[0]
    y=init[1]
    
    open = [[g,x,y]]
    expand[x][y] = g
    count = 0
    
    found = False #flagthatissetwhensearchiscomplete
    resign = False #flagsetifwecan'tfindexpand
    while not found and not resign:
        if len(open) == 0:
            resign = True
        else:
            open.sort()
            open.reverse()
            next = open.pop()
            
            g = next[0]
            x = next[1]
            y = next[2]
            #expand[x][y] = count
        if x == goal[0] and y == goal[1]:
            found=True
        else:
            for i in range(len(delta)):
                x2 = x + delta[i][0]
                y2 = y + delta[i][1]
                #print(delta_name[i])
                #print(count)
                if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                    if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                        g2 = g + cost
                        open.append([g2,x2,y2])
                        closed[x2][y2] = 1
                        #for i in range(len(expand)):
                            #print(expand[i])
                        #print(count)
                        count += 1
                        expand[x2][y2] = count
    for i in range(len(expand)):
        print(expand[i])
    #print(next)
    #print(closed)
    return expand
    
search(grid,init,goal,cost)