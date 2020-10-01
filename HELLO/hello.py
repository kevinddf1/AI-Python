import math
import itertools
import random
a=1

for i in itertools.count(start=1):
    if(i==150):
        break
    print(i)
    T=10000-math.pow(i,1.9)
    print(T)