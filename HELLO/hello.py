class Node:
    def __init__(self, state):
        self.state=state
    
    ## get the collison number
    def get_h(self):
        collisions=0
        for x in range(8):
            index=self.state[x].index(1)
            for y in range(x+1, 8):
                ##first check do we have collision in the same coloum
                if(self.state[y][index]==1):
                    collisions+=1
                ## then check the left diagonal
                l=index-(y-x) ## the index we need to check
                if(l>=0): ## make sure it's in bound
                    if(self.state[y][l]==1):
                        collisions+=1
                ## check the right diagonal
                r=index+(y-x) ## the index we need to check
                if(r<=7):
                    if(self.state[y][r]==1):
                        collisions+=1
        return collisions

def printState(arr):
    for row in arr: 
        print(row) 
    pass


testA = [[0 for i in range(8)] for j in range(8)] 
testA[0][3]=1
testA[1][2]=1
testA[2][1]=1
testA[3][4]=1
testA[4][3]=1
testA[5][2]=1
testA[6][1]=1
testA[7][2]=1
printState(testA)
nodeA= Node(testA)

nodeB=nodeA
nodeA.state[0][3]=0

print(nodeA.state)
print(nodeB.state)