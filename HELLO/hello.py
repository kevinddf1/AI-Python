from queue import PriorityQueue
from functools import total_ordering

@total_ordering
class Node:
     f=0
     h=0
     def __init__(self,  path_cost):
          self.path_cost=path_cost

     def __lt__(self, other):
          return self.f < other.f

n= Node(4)
n.f=2

m= Node(4)
m.f=3

openList=PriorityQueue()


openList.put(m)
openList.put(n)




print(openList.get().f)


# q = PriorityQueue()
# q.put(3)
# q.put(5)
# q.put(1)
# q.put(2)
# print(q.get())