import sys
import math
import time
from queue import PriorityQueue
import random 
from copy import copy, deepcopy


# Author: Fan Ding
# Email: ding0322@umn.edu
# UMN CSCI 5511 AI
# Prof: Andy Exley
# Date: 09/30/2020 


#setup
cols=8
rows=8
print("Welcome to 8-Queens Problem")


""" ---------------------------------------------------Build a Node class------------------------------------------------------------------ """


class Node:
    def __init__(self, state):
        self.state=state
    
    ## get the collison number
    def get_h(self):
        collisions=0
        for x in range(rows):
            index=self.state[x].index(1)
            for y in range(x+1, cols):
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



""" --------------------------------------local search fucntions----------------------------------- """

#That uses hill climbing with steepest-ascent to attempt to solve the problem. 
# Have your code detect a plateau or local maximum and give up if those are encountered.
def hillclimb_sa(init):
    current=Node(init)
    while(1):
        ##loop all neighbor, the the min collision
        min_neighbor= min_collision(current) ##min_collision return the neighbor with the smallest collision
        ## plateau check
        if(min_neighbor==-1):
            print("plateau detected")
            return -1
        if(current.get_h()<=min_neighbor.get_h()):
            if(current.get_h()!=0):
                print("this is a local min")
                return -1
            return current.state
        current=min_neighbor
    return -1
def min_collision(current):
    plateau=True
    min_neighbor = current
    for x in range(rows):
        index=current.state[x].index(1)
        tempState=deepcopy(current.state)
        tempState[x][index]=0
        for y in range(cols):
            temp2=deepcopy(tempState)
            temp2[x][y]=1
            ##right now the temp2 is one of the 64 neighbors states
            tempNode= Node(temp2)
            ## plateau check
            if(tempNode.get_h()!=min_neighbor.get_h()):
                plateau=False
            if(tempNode.get_h()<min_neighbor.get_h()):
                min_neighbor=tempNode
    ##plateau
    if(plateau==True):
        return -1
    return min_neighbor

#That implements first-choice hill climbing for the same problem.
def hillclimb_fc(init):
    pass

#That implements simulated annealing for the problem. Choose your temperature and schedule.
def sim_anneal(init):
    pass





""" -------------functions about genarate random initial states---------------------------- """
##genarate one state
def genarateOneState():

    arr = [[0 for i in range(cols)] for j in range(rows)] 

    for i in range(rows):
        r = random.randint(0, cols-1)
        arr[i][r]=1
       
    return arr

##print out the state in terminal
def printState(arr):
    for row in arr: 
        print(row) 
    pass



""" --------------------------------------------get_h test and hill climb functions using book examples--------------------------------- """

## this 2 example are form book page 123 
testA = [[0 for i in range(cols)] for j in range(rows)] 
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
print("the collision is "+str(nodeA.get_h())) ##should be 17
print()

##test hillclimb_sa
resultState=hillclimb_sa(testA)
if(resultState==-1):
    print("can't find a solution")
else:
    printState(resultState)
    nodeResult= Node(resultState)
    print("the collision is "+str(nodeResult.get_h())) ##should be 0
print()

##test hillclimb_fc

# testB= [[0 for i in range(cols)] for j in range(rows)] 
# testB[0][0]=1
# testB[1][5]=1
# testB[2][1]=1
# testB[3][4]=1
# testB[4][6]=1
# testB[5][3]=1
# testB[6][7]=1
# testB[7][2]=1
# printState(testB)
# nodeB= Node(testB)
# print("the collision is "+str(nodeB.get_h())) ## should be 1
# print()

# ##test hillclimb_sa
# resultState2=hillclimb_sa(testB)
# printState(resultState2)
# nodeResult2= Node(resultState2)
# print("the collision is "+str(nodeResult2.get_h())) ##should be 1
# print()

## test hillclimb_fc





""" --------------------------------main-------------------------------------------------- """

# a= genarateOneState()
# printState(a)

# hillclimb_sa(a)
# hillclimb_fc(a)
# sim_anneal(a)




















with open('readme.txt', 'w') as f:
    f.write("hello world!!!!!!!!!\n")