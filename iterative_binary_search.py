def binarySearch_iter(arr,low,high,targ): ###this is an interative method, not a recursive method, an iterative is a kind of loop method
    
    while low<=high: # not if, because it is an iterative method
        mid=(low+high)//2
        if arr[mid]==targ:
            return mid
        elif arr[mid] < targ:
            low=mid+1
        elif arr[mid] > targ:
            high=mid-1
    return -1
 
 
# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 3
 
# Function call
result = binarySearch_iter(arr, 0, len(arr)-1, x)
 
if result != -1:
    print "Element is present at index %d" % result
else:
    print "Element is not present in array"
