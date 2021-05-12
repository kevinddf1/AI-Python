import sat_interface
import random

# Author: Fan Ding
# Final problem 2
# Email: ding0322@umn.edu
# UMN CSCI 5511 AI
# Prof: Andy Exley
# Date: 12/16/2020 


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





""" ---------------- Final problem 2----------------"""
def rand3cnf(m, n):
    #print("Let's print out a random sentence in 4-CNF")
    symbol_List =['A']*n
    for i in range(1, len(symbol_List)):
        symbol_List[i]=chr(ord(symbol_List[i])+i)+""
    #print("symbol_List is :", symbol_List)
    TF_List=["", "~"]
    #print("TF_list is : ", TF_List)
   
    result=[]
    for i in range(m):
        smapling= random.sample(symbol_List, 3)
        temStr=""+random.choice(TF_List)+smapling[0]+" "+random.choice(TF_List)+smapling[1]+" "+random.choice(TF_List)+smapling[2]
        result.append(temStr)
    #print(result)
    return result



def bigLoop():
    mList=[20,30,40,50,60,70,80]
    nList=[5,10,15,20]
    print("Running...")
    for m in mList:
        for n in nList:
            print("m="+str(m)+" "+"n="+str(n))
            Tnum=0
            Fnum=0
            for i in range(100):
                myKB=rand3cnf(m, n)
                prob= sat_interface.KB(myKB)
                if(prob.is_satisfiable()==True):
                    Tnum+=1
                else:
                    Fnum+=1
            print("True: "+str(Tnum) +"              False: "+str(Fnum))
    print("Finished")








print(rand3cnf(80,5))
bigLoop()

#report: When m goes up, less satisfaction.
#        Because more clauses brings more contriction for Knowlegebase, 
#        which causes more conflicts.
#
#        when n goes up, more satisfaction.
#        Because more symbols brings more total possible combinations,
#        which  causes less conflicts.