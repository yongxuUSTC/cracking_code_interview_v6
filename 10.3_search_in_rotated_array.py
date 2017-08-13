###CCI6 10.3 Search in Rotated Array
class SearchRotated(object):
    def __init__(self):
        pass
    
    def binarySearch(self, arr, targ):
        inf_ind=self.findInflectionIndex(arr)
        print "inflection point index", inf_ind
        
        if (targ >= arr[inf_ind]) and (targ <=arr[-1]):
            targ_ind=self.quicksearch(arr, inf_ind, len(arr)-1,targ)
        else:
            targ_ind=self.quicksearch(arr, 0, inf_ind-1, targ)
        return targ_ind
    
    def findInflectionIndex(self,arr):
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                inf_ind=i+1
                return i+1 # find the inflection point index
        return 0 # in natural order
    
    # def quicksearch(self, arr,targ):
    #     mid_ind=len(arr)//2
    #     if arr[mid_ind] == targ:
    #         return mid_ind #this is a bug, because it is changed dynamically
    #     elif arr[mid_ind] > targ:
    #         self.quicksearch(arr[:mid_ind],targ) #this is not good, because the arr is changed dynamically, the find index is not the actual index
    #     elif arr[mid_ind] < targ:
    #         self.quicksearch(arr[mid_ind:],targ)
    #     return False
        
    def quicksearch(self, arr, low, high,targ):
        if high >= low:
            mid=(low+high)//2 
            if arr[mid] == targ:
                #print mid
                return mid
            elif arr[mid] > targ:
                #self.quicksearch(arr, low, mid-1, targ)  # bug, i should return the results from the low-low-low level
                return self.quicksearch(arr, low, mid-1, targ)
            elif arr[mid] < targ:
                #self.quicksearch(arr, mid+1, high, targ) # big bug, i should return the results from the low-lowlow level
                return self.quicksearch(arr, mid+1, high, targ)
        else:
            return -1

def main():
    arr=[15,16,19,20,25,1,3,4,5,7,10,14]
    ts=SearchRotated()
    tar_ind= ts.binarySearch(arr,7)
    print "target index:", tar_ind

if __name__=='__main__':
    main()
