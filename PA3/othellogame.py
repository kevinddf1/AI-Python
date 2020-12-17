# Author: Fan Ding
# Email: ding0322@umn.edu
# UMN CSCI 5511 AI
# Prof: Andy Exley
# Date: 10/06/2020 


'''
othellogame module

sets up an Othello game closely following the book's framework for games

OthelloState is a class that will handle our state representation, then we've 
got stand-alone functions for player, actions, result and terminal_test

Differing from the book's framework, is that utility is *not* a stand-alone 
function, as each player might have their own separate way of calculating utility


'''
import copy
import random
import math


WHITE = 1
BLACK = -1
EMPTY = 0
SIZE = 8
SKIP = "SKIP"
positive_infnity = float('inf') 
negative_infnity = float('-inf') 


class OthelloPlayerTemplate:
    '''Template class for an Othello Player

    An othello player *must* implement the following methods:

    get_color(self) - correctly returns the agent's color

    make_move(self, state) - given the state, returns an action that is the agent's move
    '''
    def __init__(self, mycolor):
        self.color = mycolor

    def get_color(self):
        return self.color

    def make_move(self, state):
        '''Given the state, returns a legal action for the agent to take in the state
        '''
        return None

""" ---------------------------------My code: RandomPlayer--------------------------------- """

class RandomPlayer:
    def __init__(self, mycolor):
        self.color = mycolor

    def get_color(self):
        return self.color

    def make_move(self, state):
        curr_move = None
        legals = actions(state)
        display(state)
        if self.color == 1:
            print("White ", end='')
        else:
            print("Black ", end='')
        print(" to play.")
        print("Legal moves are " + str(legals))
        randIndex= random.randint(0, len(legals)-1)
        print("we picked a random move "+ str(legals[randIndex]))
        curr_move = legals[randIndex]
        return curr_move


""" ---------------------------------My code: UtilityFunction------------------------------ """
def UtilityFunction(state):
    if(state==None):
        return None
    
    player = state.current
    
    wcount = 0
    bcount = 0
    for i in range(SIZE):
        for j in range(SIZE):
            if state.board_array[i][j] == WHITE:
                wcount += 1
            elif state.board_array[i][j] == BLACK:
                bcount += 1

    if(player.get_color()==WHITE):
        leading= wcount-bcount
    else:
        leading= bcount-wcount

    if(terminal_test(state)):
        leading=leading*1000
    
    return leading

 

""" ---------------------------------My code: MinimaxPlayer------------------------------ """

class MinimaxPlayer:
    def __init__(self, mycolor, depth):
        self.color = mycolor
        self.depth = depth
    
    def get_color(self):
        return self.color

    def make_move(self, state):

        def MiniMax_Decision(state):
            temp_max=negative_infnity
            act=None
            for x in range(len(legals)): 
                r=Min_value(result(state, legals[x]), 1)
                if r>temp_max:
                    temp_max=r
                    act= legals[x]
            return act
            
        def Max_value(state, depthcounter):
            legals = actions(state)
            if (terminal_test(state) or depthcounter==self.depth):
                return UtilityFunction(state)
            v = negative_infnity
            for x in range(len(legals)):
                v = max(v, Min_value(result(state, legals[x]), depthcounter+1))
            return v

        def Min_value(state, depthcounter):
            legals = actions(state)
            if (terminal_test(state) or depthcounter==self.depth):
                return UtilityFunction(state)
            v = positive_infnity
            for x in range(len(legals)):
                v = min(v, Max_value(result(state, legals[x]), depthcounter+1))
            return v

        curr_move = None
        legals = actions(state)
        display(state)
        if self.color == 1:
            print("White ", end='')
        else:
            print("Black ", end='')
        print(" to play.")
        print("Legal moves are " + str(legals))
        curr_move = MiniMax_Decision(state)
        print("we picked a optimal move "+ str(curr_move))
        return curr_move







""" ---------------------------------My code: AlphabetaPlayer--------------------------------- """

class AlphabetaPlayer:
    def __init__(self, mycolor, depth):
        self.color = mycolor
        self.depth = depth

    def get_color(self):
        return self.color

    def make_move(self, state):
        def alpha_beta_search(state):
            result= Max_value(state, 0, negative_infnity, positive_infnity)##result is [untility, action]
            return result[1]
            
        def Max_value(state, depthcounter, alpha, beta):
            legals = actions(state)
            act=None
            if (terminal_test(state) or depthcounter==self.depth):
                return UtilityFunction(state), act
            v = negative_infnity

            for x in range(len(legals)): 
                tem=Min_value(result(state, legals[x]), depthcounter+1, alpha, beta)
                r=tem[0]
                if r>v:
                    v=r
                    act= legals[x] 

                if v>=beta:
                    return v, act
                alpha=max(alpha, v)
            return v, act

        def Min_value(state, depthcounter, alpha, beta):
            legals = actions(state)
            act=None
            if (terminal_test(state) or depthcounter==self.depth):
                return UtilityFunction(state), act
            v = positive_infnity

            for x in range(len(legals)): 
                tem=Min_value(result(state, legals[x]), depthcounter+1, alpha, beta)
                r=tem[0]
                if r<v:
                    v=r
                    act= legals[x] 
                
                if v<=alpha:
                    return v, act
                beta= min(beta, v)
            return v , act

        curr_move = None
        legals = actions(state)
        display(state)
        if self.color == 1:
            print("White ", end='')
        else:
            print("Black ", end='')
        print(" to play.")
        print("Legal moves are " + str(legals))
        curr_move = alpha_beta_search(state)
        print("we picked a optimal move "+ str(curr_move))
        return curr_move



class HumanPlayer:
    def __init__(self, mycolor):
        self.color = mycolor

    def get_color(self):
        return self.color

    def make_move(self, state):
        curr_move = None
        legals = actions(state)
        while curr_move == None:
            display(state)
            if self.color == 1:
                print("White ", end='')
            else:
                print("Black ", end='')
            print(" to play.")
            print("Legal moves are " + str(legals))
            move = input("Enter your move as a r,c pair:")
            if move == "":
                return legals[0]

            if move == SKIP and SKIP in legals:
                return move

            try:
                movetup = int(move.split(',')[0]), int(move.split(',')[1])
            except:
                movetup = None
            if movetup in legals:
                curr_move = movetup
            else:
                print("That doesn't look like a legal action to me")
        return curr_move




class OthelloState:
    '''A class to represent an othello game state'''

    def __init__(self, currentplayer, otherplayer, board_array = None, num_skips = 0):
        if board_array != None:
            self.board_array = board_array
        else:
            self.board_array = [[EMPTY] * SIZE for i in range(SIZE)]
            self.board_array[3][3] = WHITE
            self.board_array[4][4] = WHITE
            self.board_array[3][4] = BLACK
            self.board_array[4][3] = BLACK
        self.num_skips = num_skips
        self.current = currentplayer
        self.other = otherplayer


def player(state):
    return state.current

def actions(state):
    '''Return a list of possible actions given the current state
    '''
    legal_actions = []
    for i in range(SIZE):
        for j in range(SIZE):
            if result(state, (i,j)) != None:
                legal_actions.append((i,j))
    if len(legal_actions) == 0:
        legal_actions.append(SKIP)
    return legal_actions

def result(state, action):
    '''Returns the resulting state after taking the given action

    (This is the workhorse function for checking legal moves as well as making moves)

    If the given action is not legal, returns None

    '''
    # first, special case! an action of SKIP is allowed if the current agent has no legal moves
    # in this case, we just skip to the other player's turn but keep the same board
    if action == SKIP:
        newstate = OthelloState(state.other, state.current, copy.deepcopy(state.board_array), state.num_skips + 1)
        return newstate

    if state.board_array[action[0]][action[1]] != EMPTY:
        return None

    color = state.current.get_color()
    # create new state with players swapped and a copy of the current board
    newstate = OthelloState(state.other, state.current, copy.deepcopy(state.board_array))

    newstate.board_array[action[0]][action[1]] = color
    
    flipped = False
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    for d in directions:
        i = 1
        count = 0
        while i <= SIZE:
            x = action[0] + i * d[0]
            y = action[1] + i * d[1]
            if x < 0 or x >= SIZE or y < 0 or y >= SIZE:
                count = 0
                break
            elif newstate.board_array[x][y] == -1 * color:
                count += 1
            elif newstate.board_array[x][y] == color:
                break
            else:
                count = 0
                break
            i += 1

        if count > 0:
            flipped = True

        for i in range(count):
            x = action[0] + (i+1) * d[0]
            y = action[1] + (i+1) * d[1]
            newstate.board_array[x][y] = color

    if flipped:
        return newstate
    else:  
        # if no pieces are flipped, it's not a legal move
        return None

def terminal_test(state):
    '''Simple terminal test
    '''
    # if both players have skipped
    if state.num_skips == 2:
        return True

    # if there are no empty spaces
    empty_count = 0
    for i in range(SIZE):
        for j in range(SIZE):
            if state.board_array[i][j] == EMPTY:
                empty_count += 1
    if empty_count == 0:
        return True
    return False

def display(state):
    '''Displays the current state in the terminal window
    '''
    print('  ', end='')
    for i in range(SIZE):
        print(i,end='')
    print()
    for i in range(SIZE):
        print(i, '', end='')
        for j in range(SIZE):
            if state.board_array[j][i] == WHITE:
                print('W', end='')
            elif state.board_array[j][i] == BLACK:
                print('B', end='')
            else:
                print('-', end='')
        print()
    # print("btw, now player's color is " + str(state.current.get_color()))
    # print("btw, and his/her leading socre is " + str(UtilityFunction(state)))



def display_final(state):
    '''Displays the score and declares a winner (or tie)
    '''
    wcount = 0
    bcount = 0
    for i in range(SIZE):
        for j in range(SIZE):
            if state.board_array[i][j] == WHITE:
                wcount += 1
            elif state.board_array[i][j] == BLACK:
                bcount += 1

    print("Black: " + str(bcount))
    print("White: " + str(wcount))
    if wcount > bcount:
        print("White wins")
    elif wcount < bcount:
        print("Black wins")
    else:
        print("Tie")

def play_game(p1 = None, p2 = None):
    '''Plays a game with two players. By default, uses two humans
    '''
    if p1 == None:
        p1 = HumanPlayer(BLACK)
    if p2 == None:
        p2 = HumanPlayer(WHITE)

    s = OthelloState(p1, p2)
    while True:
        action = p1.make_move(s)
        if action not in actions(s):
            print("Illegal move made by Black")
            print("White wins!")
            return
        s = result(s, action)
        if terminal_test(s):
            print("Game Over")
            display(s)
            display_final(s)
            return
        action = p2.make_move(s)
        if action not in actions(s):
            print("Illegal move made by White")
            print("Black wins!")
            return
        s = result(s, action)
        if terminal_test(s):
            print("Game Over")
            display(s)
            display_final(s)
            return

""" ---------------------------------------------------tests----------------------------------------- """
def main():
    #Human Player vs Human Player
    #play_game()

    #Human player against random machine player
    #play_game(HumanPlayer(BLACK), RandomPlayer(WHITE))

    #random player against minimaxplayer
    #play_game(RandomPlayer(BLACK), MinimaxPlayer(WHITE, 2))


    #random player against alphabetplayer
    play_game(RandomPlayer(BLACK), AlphabetaPlayer(WHITE , 7))

if __name__ == '__main__':
    main()

