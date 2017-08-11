###10.1 CCI6 Soreted Merge
class SortedMerge(object):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def sm_method1(self):
        self.a.extend(self.b)
        #x=sorted(self.a) # can not sorted in-place
        #return x
        self.a.sort() # can be sorted in-place, because it is the method of list
        return self.a
    
    def sm_method2(self):
        
        # #special cases
        # if (self.b[0])>=self.a[-1]:
        #     self.a.extend(self.b)
        #     return self.a 
        # elif (self.b[0]<=self.a[0]):
        #     self.b.extend(self.a)
        #     return self.b 
        # 
        # j=0
        # for i in range(len(b)):
        #     while(j< range(len(a))):
        #         if b[i]>=a[j] and b[i]<a[j+1]:
        #             a.insert(j,b[i]) # this is totally wrong idea to inser like this, it will make the length of 'a' dynamic variable
        
        #this is in fact the merge-sort sub-problem
        ia=0
        ib=0
        c=[]
        flaga=0
        flagb=0
        #print self.a 
        #print self.b
        #while((ia<len(self.a) & ib < len(self.b))): #bug: & can not be used for and , it only for bit manipulation
        while((ia<len(self.a) and ib < len(self.b))):      
            #print ia
            if self.a[ia]<=self.b[ib]:
                c.append(self.a[ia])
                ia += 1
                if ia >= len(self.a):
                    flaga=1
            else:
                c.append(self.b[ib])
                ib += 1
                if ib>=len(self.b):
                    flagb=1
        if (flaga == 1):
            c.extend(self.b[ib:])
        elif (flagb == 1):
            c.extend(self.a[ia:])
        return c

def main():
    a=[1,4,5,6]
    b=[2,3,5]
    ts=SortedMerge(a,b)
    #print "method1 results:"
    #print ts.sm_method1()
    print "method2 results:"
    print ts.sm_method2()
        

if __name__=='__main__':
    main()
