# 8.12 Eight queens using backtracking method
# back-tracking method is interesting, as it is like making a trial first, and then check back whether this decision is wise or not
# is it like a simple reinforcement learning ?

import numpy

class Nqueens(object):
    def __init__(self):
        pass
    
    def print_board(self,board):
        for i in range(len(board)):
            for j in range(len(board)):
                print board[i][j], # here the comma is important to print each element following with a blank space
            print "\n" # or just "print" is also fine
    
    def isSafe(self, board, row, col):
        
        #check the current row on the left of "col"
        for i in range(col):   # it is no need to check the whole current col, because each col only has one queen, and the above will not have, or it can not get here; and the below also will not have because it has not reached there
            if board[row][i]==1:
                return False
        
        #check the above left side of the current node
        for i,j in zip(range(row,-1,-1),range(col,-1,-1)): #zip will return tuples; zip(*zipped) will unzip
            if board[i][j]==1:
                return False
        
        #check the below left side of the current node
        for i,j in zip(range(row,len(board),1),range(col,-1,-1)):
            if board[i][j]==1:
                return False 
        
        return True  ###my bug, i forgot it, if there is no False cases, i shoul return true!!!
    
    def solveNQutil(self, board, col):
        
        if col >= len(board):
            self.print_board(board)
            print
           #return True # only print the first solution
            return False # print all solutions #the base or stop case when  we successfully find a solution
        
        #print len(board)
        for i in range(len(board)): # traverse the whole rows
            #print i
            if self.isSafe(board, i,col):
                board[i][col]=1 #set to 1 based on the history, not the future feasibility
                
                if self.solveNQutil(board, col+1) is True:
                    return True #break the for-loop
                
                board[i][col]=0 # set back to 0, because the future feasibility is not possible, it did not lead to a solution
            
        return False 

def main():
    ts=Nqueens()
    N=4
    board=numpy.zeros((N,N),dtype='int')
    ts.solveNQutil(board,0)
    #ts.print_board(board)

if __name__ == '__main__':
    main()
            
