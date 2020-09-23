import sys
import math
import time
from queue import PriorityQueue


# Author: Fan Ding
# Email: ding0322@umn.edu
# UMN CSCI 5511 AI
# Prof: Andy Exley
# Date: 09/22/2020 




#setup problem
input=sys.argv[1]

#Make PuzzleList from the input integer number
PuzzleList=[int(x) for x in str(input)] 
checklist= PuzzleList.copy()
checklist.sort()
if(checklist!=[0,1,2,3,4,5,6,7,8]):
    print("wrong type of input, check your input and restart")
    exit()



#inportant variables
SolutionPuzzle= [1,2,3,8,0,4,7,6,5]





""" ---------------------------------------------------Build a Node class------------------------------------------------------------------ """


class Node:
    f=0
    h=0
    def __init__(self, list, parent, action, path_cost):
        self.list=list
        self.parent=parent
        self.action=action
        self.path_cost=path_cost


    def __lt__(self, other): 
        return self.f < other.f


    
""" -----------------------------------------------------helper functions---------------------------------------------------------------- """


def visualize(n):
    if n==None:
        print("Null")
    else:
        for x in range (9):
            print (n.list[x], end = ' ')
            if (x+1)%3==0:
                print()


def child_node(parent, action):

    #swap 2 elements in a list
    def swap(list, pos1, pos2):
        temp= list[pos1]
        list[pos1]=list[pos2]
        list[pos2]=temp

    list=parent.list.copy()
    i= list.index(0)

    ## illegal moves, return None
    if math.floor(i/3)==0 and action=="D":
        return None
    if i%3==2 and action =="L":
        return None
    if math.floor(i/3)==2 and action == "U":
        return None
    if i%3==0 and action =="R":
        return None

    ## legal move, we return a child
    if action=="D":
        swap(list, i, i-3)
    if action=="L":
        swap(list, i, i+1)
    if action=="U":
        swap(list, i, i+3)
    if action=="R":
        swap(list, i, i-1)
    return Node(list, parent, action, parent.path_cost+1)


## Go back until the root, find a path of actions
def Solution(node):
    result=[]
    while node.parent!=None:
        result.append(node.action)
        node= node.parent
    result.reverse()
    print(result)
    return "Success"

""" --------------------------------------------------Testers for helper functions------------------------------------------------------------------- """

#test visualize
def Test_Visulaize():
    print()
    print("test visualize")
    node = Node(SolutionPuzzle, None, None, 0)
    visualize(node)

#test child_node
def Test_Child_Node():
    print()
    print("test child_node")
    parent = Node(PuzzleList, None, None, 0)
    visualize(parent)
    child= child_node(parent, "U")
    print()
    visualize(child)
    print()


#Test_Visulaize()
#Test_Child_Node()


""" ----------------------------------------------------- Uninformed Search functions---------------------------------------------------------------- """



# BFS
def BFS(PuzzleList):
    node = Node(PuzzleList, None, None, 0)
    if(node.list==SolutionPuzzle):
        return Solution(node)
    queue=[]
    queue.append(node)
    explored =set()
    while queue:
        s= queue.pop(0)
        if (s ==None):
            pass
        elif (''.join(map(str,s.list)) in explored):
            pass
        else:
            explored.add(''.join(map(str,s.list)))
            if(s.list==SolutionPuzzle):
                return Solution(s)
            queue.append(child_node(s, "U"))
            queue.append(child_node(s, "D"))
            queue.append(child_node(s, "L"))
            queue.append(child_node(s, "R"))
    return None


# DFS
def DFS(PuzzleList):
    node = Node(PuzzleList, None, None, 0)
    if(node.list==SolutionPuzzle):
        return Solution(node)
    stack=[]
    stack.append(node)
    explored =set()
    while stack:
        s= stack.pop(0)
        if (s ==None):
            pass
        elif (''.join(map(str,s.list)) in explored):
            pass
        else:
            explored.add(''.join(map(str,s.list)))
            if(s.list==SolutionPuzzle):
                return Solution(s)
            stack.append(child_node(s, "U"))
            stack.append(child_node(s, "D"))
            stack.append(child_node(s, "L"))
            stack.append(child_node(s, "R"))
    return None
 




#DLS
def DLS(PuzzleList, limit):
    node = Node(PuzzleList, None, None, 0) 
    return DLS_Helper(node, limit)

def DLS_Helper(node, limit):
    if node==None:
        return "failure"
    if(node.list==SolutionPuzzle):
        return Solution(node)
    elif limit<=0:
        return "cutoff"
    else:
        cutoff_occurred=False
        for act in ["U", "D","L", "R"]:
            child=child_node(node, act)
            if(child==None):
                pass
            else:
                result= DLS_Helper(child, limit-1)
                if result=="cutoff":
                    cutoff_occurred=True
                elif result!="failure":
                    return result
        if (cutoff_occurred):
            return "cutoff"
        else:
            return "failure"





#IDDFS
def iterative_deepening(PuzzleList):
    depth=-1
    while True:
        depth=depth+1
        result= DLS(PuzzleList, depth)
        if result!="cutoff":
            return result
            







""" --------------------------------------------------------------informed Search--------------------------------------------------------------------------------"""
## num_wrong_tiles:which counts the number of tiles in the wrong location
def num_wrong_tiles(PuzzleList):
    counter=0
    for i in range(9):
        if(PuzzleList[i]!=SolutionPuzzle[i]):
            counter+=1
    return counter



## manhattan_distance: which calculates the total manhattan distance for all tiles to move to their correct locations
def manhattan_distance(PuzzleList):
    counter=0
    for i in range(9):
        a=PuzzleList.index(i)
        b=SolutionPuzzle.index(i)
        if(a!=b):
            sub=abs(a-b)
            move=math.floor(sub/3)+sub%3
            counter+=move
    return counter





## A * search
def astar(PuzzleList, functionName):
    node = Node(PuzzleList, None, None, 0)
    openList=PriorityQueue()
    explored=set()
    openList.put(node)
    explored.add(''.join(map(str,node.list)))
    while not openList.empty():
        q= openList.get()
        if(q.list==SolutionPuzzle):
            return Solution(q)
        for act in ["U", "D","L", "R"]:
            child=child_node(q, act)
            if(child==None):
                pass
            elif (''.join(map(str,child.list)) in explored):
                pass
            else:
                explored.add(''.join(map(str,child.list)))
                if(functionName=="num_wrong_tiles"):
                    child.h=num_wrong_tiles(child.list)
                elif(functionName=="manhattan_distance"):
                    child.h=manhattan_distance(child.list)
                else:
                    print("wrong functionName was inputed")
                child.f=child.h+child.path_cost      
                openList.put(child)
        

""" -----------------------------------------------------------------main---------------------------------------------------------------"""

print("Here is your input Puzzel:")
n = Node(PuzzleList, None, None, 0) 
visualize(n)




#DFS TEST
print()
print("Depth-First Search result:")
start = time.process_time()   
DFS(PuzzleList)
print("time take: " + str(time.process_time() - start))


#IDDFS TEST
print()
print("Iterative Deepening result:")
start = time.process_time() 
iterative_deepening(PuzzleList)
print("time take: " + str(time.process_time() - start))


# A* Test
print()
print("A* on num_wrong_tiles ")
start = time.process_time() 
astar(PuzzleList, "num_wrong_tiles")
print("time take: " + str(time.process_time() - start))

print()
print("A* on manhattan_distance ")
start = time.process_time() 
astar(PuzzleList, "manhattan_distance")
print("time take: " + str(time.process_time() - start))