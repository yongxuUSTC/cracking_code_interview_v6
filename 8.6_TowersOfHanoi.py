### CCI6 8.6 Towers of Hanoi
import sys 
# first, we should construct a multi-stack class 
class MultiStack(object):
    def __init__(self, total_stacknum, stacksize):
        self.total_stacknum=total_stacknum  # how many stacks
        self.stacksize=stacksize # size for each stack, all the same size
        self.array=[0]*(total_stacknum * stacksize) # multistack is stored in the same array/list
        self.sizes=[0]*total_stacknum # size array to save the size for each stack
        self.minvals=[sys.maxint] *(total_stacknum * stacksize) # same size with the array, record the minist val, but why not use a three dimension list ? is it a waste of the space?
        
    def isFull (self, stacknum):
        return self.sizes[stacknum] == self.stacksize  # each subfunc should return something
    # raise Exception('The stack is full')
        
    def isEmpty (self,stacknum):
        return self.sizes[stacknum] == 0
    
    def indexoftop(self,stacknum):
        offset=stacknum * self.stacksize
        return offset+self.sizes[stacknum]-1
        
    def push(self, item, stacknum):
        if self.isFull(stacknum): # should self.subfunc
            raise Exception('The stack is full')
        self.sizes[stacknum] += 1
        if self.isEmpty(stacknum):
            self.minvals[self.indexoftop[stacknum]]=item
        else:
            #self.minvals[self.indexoftop[stacknum]]=min(item, self.minvals(self.indexoftop[stacknum]-1)) ### bug , list should use [], not ();; func should use ()
            self.minvals[self.indexoftop(stacknum)]=min(item, self.minvals[self.indexoftop(stacknum)-1])
        self.array[self.indexoftop(stacknum)]=item
    
    def pop (self,stacknum):
        if self.isEmpty(stacknum):
            raise Exception('The stack is empty')
        value=self.array[self.indexoftop(stacknum)]
        self.array[self.indexoftop(stacknum)]=0
        self.sizes[stacknum]-=1
        return value 
    
    def peek(self,stacknum):
        if self.isEmpty(stacknum):
            raise Exception('The stack is empty')
        return self.array[self.indexoftop(stacknum)]
    
    def size(self,stacknum):
        return self.size(stacknum)
            
    def min(self,stacknum):
        return self.minvals[self.indexoftop(stacknum)]        

def movetower(N,start,end,buff,stack): # N is the disk number
    if N==1:
        stack.push(stack.pop(start),end) # func should use ()
    else:
        movetower(N-1, start, buff, end, stack) # the recursion is just like there is two or three case, you should 
        movetower(1, start, end, buff, stack) #
        movetower(N-1, buff, end, start, stack) #

def main():
    #fill in a multistack
    disknum=6
    total_stacknum=3
    mst=MultiStack(total_stacknum, disknum)
    for item in range(disknum, 0,-1): # to get size 3, 2, 1 disk, 0 is not inculsive
        mst.push(item, 0)
    
    movetower(disknum, 0, 2, 1, mst)
    
    #print the target tower
    for item in range (disknum):
        #print (''.join(['-' for _ in range(mst.pop(stacknum))])) #bug: stacknum is the total number of stack, not the index of the specified stack
        print (''.join(['-' for _ in range (mst.pop(2))]))

if __name__=='__main__':
    main()
