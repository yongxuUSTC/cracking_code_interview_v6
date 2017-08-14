###CCI6 Sparse search on strings
def sparseSearchStr(strs,targ, low, high):
    if low<=high:
        mid=(low+high)//2
        print "old mid:", mid
        
        if strs[mid]=="":
            left=mid-1
            right=mid+1
            while(1):
                if (left < low and right > high):
                    return -1   # can not find
                elif ((right <=high) and (not strs[right] == "")):
                    mid=right
                    break 
                elif ((left>=low) and (not strs[left] == "")):
                    mid=left
                    break
                left -=1
                right +=1
        print "new mid:" , mid
        
        if strs[mid]==targ:  #it only can be set here, because the above mid has been changed
            print "equal, ", strs[mid], targ
            return mid       
        elif (targ < strs[mid]):
            return sparseSearchStr(strs,targ, low, mid-1)
        elif targ > strs[mid]:
            return sparseSearchStr(strs,targ,mid+1,high)
        return -1

#driver program
strs=["at","","","","ball","","","car","","","dad","",""]
targ="car"
targ_index=sparseSearchStr(strs,targ,0,len(strs))
print targ_index
