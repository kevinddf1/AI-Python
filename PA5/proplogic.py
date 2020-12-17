import sat_interface

# Author: Fan Ding
# Email: ding0322@umn.edu
# UMN CSCI 5511 AI
# Prof: Andy Exley
# Date: 11/12/2020 


def showResult(thislist, example_prob):
    for x in thislist:
        xIs=example_prob.test_literal(x)
        xNot=example_prob.test_literal("~"+x)
        print(x+" is " + decide(xIs, xNot))



def decide(a, b):
    if(a==True and b==False):
        return "Truth-teller"
    elif(a==False and b== True):
        return "liar"
    else:
        return "not sure"

# print()
# print("problem 1")
# example_prob = sat_interface.KB(["~A ~B", "B A", "~B ~C", "C B", "~C ~A", "~C ~B", "A B C"])
# print(example_prob.is_satisfiable())
# thislist = ["A", "B", "C"]
# showResult(thislist, example_prob)



""" ------------problem 2----------------------------------------- """
def tt2():
    print()
    print("problem 2")
    example_prob2 = sat_interface.KB(["~A C", "~B ~C", "C B", "~C B ~A", "~B C", "A C"])
    #print(example_prob2.is_satisfiable())
    thislist2 = ["A", "B", "C"]
    showResult(thislist2, example_prob2)




""" ------------problem 3----------------------------------------- """
def tt3():
    print()
    print("problem 3")
    example_prob3 = sat_interface.KB(["~A ~C", "C A", "~B ~A", "~B ~C", "A C B", "~C B", "~B C"])
    #print(example_prob3.is_satisfiable())
    thislist3 = ["A", "B", "C"]
    showResult(thislist3, example_prob3)


""" ------------problem 4----------------------------------------- """
def salt():
    print()
    print("problem 4")
    example_prob4 = sat_interface.KB(["a b c", "~a ~b", "~a ~c",  "~c ~b", "~A ~B ~C", "A B C", "~A b", "~B A", "~C ~c", "~b A", "~A B", "c C"])
    #print(example_prob4.is_satisfiable())
    thislist4 = ["A", "B", "C" ,"a", "b", "c"]
    showResult(thislist4, example_prob4)
    print("----------caterpillar ate the salt---------")


""" --------------problem 5------------------------------ """
def golf():
    print()
    print("problem 5")
    example_prob5 = sat_interface.KB(["~aT bH", "~aH ~bH", "~bT bD", "~bH ~bD", "~cT bT", "~cH ~bT", 
                                        "aT bT cT", "~aT ~bT", "~aT ~cT", "~bT ~cT",
                                        "aH bH cH", "~aH ~bH", "~aH ~cH", "~bH ~cH",
                                        "aD bD cD", "~aD ~bD", "~aD ~cD", "~bD ~cD",
                                        "aT aH aD", "~aT ~aH", "~aT ~aD", "~aH ~aD",
                                        "bT bH bD", "~bT ~bH", "~bT ~bD", "~bH ~bD",
                                        "cT cH cD", "~cT ~cH", "~cT ~cD", "~cH ~cD",])
    #print(example_prob5.is_satisfiable())
    thislist5 = ["aH", "bH", "cH","aD", "bD", "cD","aT", "bT", "cT"]
    showResult(thislist5, example_prob5)
    print("-----------Tom, Harry, Dick------------")



tt2()
tt3()
salt()
golf()