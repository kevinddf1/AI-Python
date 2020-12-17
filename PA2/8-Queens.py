import sys
import math
import time
from queue import PriorityQueue
import random 
from copy import copy, deepcopy
import itertools

# Author: Fan Ding
# Email: ding0322@umn.edu
# UMN CSCI 5511 AI
# Prof: Andy Exley
# Date: 09/30/2020 


#setup
cols=8
rows=8
print("Welcome to 8-Queens Problem")
print()


""" --------------------------------------------Build a Node class---------------------------------- """


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

""" ------------------------------------print the state function for debug------------------------------- """
##print out the state in terminal
def printState(arr):
    for row in arr: 
        print(row) 
    pass


""" --------------------------------------hillclimb_sa-------------------------------------------------- """

#That uses hill climbing with steepest-ascent to attempt to solve the problem. 
# Have your code detect a plateau or local maximum and give up if those are encountered.
def hillclimb_sa(init):
    step=0
    current=Node(init)
    while(1):
        step+=1
        ##loop all neighbor, the the min collision
        min_neighbor= min_collision(current) ##min_collision return the neighbor with the smallest collision
        ## plateau check
        if(min_neighbor==-1):
            #print("plateau detected")
            return -1
        if(current.get_h()<=min_neighbor.get_h()):
            if(current.get_h()!=0):
                #print("this is a local min")
                return -1
            return current.state, step
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


""" --------------------------------------hillclimb_fc---------------------------------------------- """
#That implements first-choice hill climbing for the same problem.
def hillclimb_fc(init):
    step=0
    current=Node(init)
    
    while(1):
        step+=1
        ##this generate 64 numbers in random order, each number is represent to one neighbor
        randomMoveList=random.sample(range(0, 64), 64)
        count=0
        nextNode=generate_neighbor(current, randomMoveList[count])
        while(nextNode.get_h()>=current.get_h()):
            if(count==63):
                if(current.get_h()!=0):
                #print("this is a local min")
                    return -1
                return current.state, step
            count+=1
            nextNode=generate_neighbor(current, randomMoveList[count])
        current=nextNode
    return -1

def generate_neighbor(current, randMove):
    x= math.floor(randMove/8)
    y=randMove%8
    tempState=deepcopy(current.state)
    tempState[x][tempState[x].index(1)]=0 ## make the 1 in x row 0
    tempState[x][y]=1
    result=Node(tempState)
    return result


""" --------------------------------------sim_anneal-------------------------------------------------- """

#That implements simulated annealing for the problem. Choose your temperature and schedule.
def sim_anneal(init):
    step=0
    current=Node(init)
    for i in itertools.count(start=1):
        if(current.get_h()==0):
            return current.state, step
        T=0.01/math.log10(i+1)
        if (i==1000):
            return -1
        child= generate_neighbor(current, random.randint(0, 63))
        deltaE= child.get_h()-current.get_h()
        if(deltaE<0):
            step+=1
            current=child
        elif(random.uniform(0, 1)<=math.exp(-deltaE/T)):
            step+=1
            current=child
    return -1











""" ------------------------------testers using one book example------------------------- """

## this example is form book page 123 
testA = [[0 for i in range(cols)] for j in range(rows)] 
testA[0][3]=1
testA[1][2]=1
testA[2][1]=1
testA[3][4]=1
testA[4][3]=1
testA[5][2]=1
testA[6][1]=1
testA[7][2]=1
print("Here is the given input state:")
printState(testA)
nodeA= Node(testA)
print("the collision is "+str(nodeA.get_h())) ##should be 17
print()


# test hillclimb_sa
print("hillclimb_sa:")
resultState=hillclimb_sa(testA)
if(resultState==-1):
    print("can't find a solution")
else:
    printState(resultState[0])
    nodeResult= Node(resultState[0])
    print("solution found, detected solution collision is "+str(nodeResult.get_h())) ##should be 0
print()

# test hillclimb_fc
print("hillclimb_fc:")
resultState=hillclimb_fc(testA)
if(resultState==-1):
    print("didn't find a solution")
else:
    printState(resultState[0])
    nodeResult= Node(resultState[0])
    print("solution found, detected solution collision is "+str(nodeResult.get_h())) ##should be 0
print()

# test sim_anneal
print("sim_anneal:")
resultState=sim_anneal(testA)
if(resultState==-1):
    print("didn't find a solution")
else:
    printState(resultState[0])
    nodeResult= Node(resultState[0])
    print("solution found, detected solution collision is "+str(nodeResult.get_h())) ##should be 0
print()



""" ------------------------functions about genarate random initial states---------------------------- """
##genarate one state
def genarateOneState():

    arr = [[0 for i in range(cols)] for j in range(rows)] 

    for i in range(rows):
        r = random.randint(0, cols-1)
        arr[i][r]=1
       
    return arr

""" ------------------------------------------main-------------------------------------------------- """
# this program generate many random initial states and test them with 3 different search alg to find the ave steps of them

many=100
print("running tests on "+ str(many)+  " random initial states...\n")
print()
with open('readme.txt', 'w') as f:
    success_num_sa=0
    success_num_fc=0
    success_num_sim=0
    success_total_step_sa=0
    success_total_step_fc=0
    success_total_step_sim=0

    for x in range(many):
        a= genarateOneState()
        result_sa=hillclimb_sa(a)
        result_fc=hillclimb_fc(a)
        result_sim=sim_anneal(a)
        if(result_sa!=-1):
            success_num_sa+=1
            success_total_step_sa+=result_sa[1]
        if(result_fc!=-1):
            success_num_fc+=1
            success_total_step_fc+=result_fc[1]  
        if(result_sim!=-1):
            success_num_sim+=1
            success_total_step_sim+=result_sim[1]  


    tempS="Here is the report for our local search: "+ "\n" +"and we used "+str(many)+" random initial states to test them\n\n"
    f.write(tempS)
    tempS = "hillclimb_sa average step: "+str(success_total_step_sa/success_num_sa)+" \n"
    f.write(tempS)
    tempS = "hillclimb_fc average step: "+str(success_total_step_fc/success_num_fc)+" \n"
    f.write(tempS)
    tempS = "sim_anneal average step: "+str(success_total_step_sim/success_num_sim)+" \n"
    f.write(tempS)

    print("Finished running. Check out the readme.txt to see report details")






















