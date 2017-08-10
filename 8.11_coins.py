### method1, time: O(nm); space O(nm)
# Dynamic Programming Python implementation of Coin Change problem
def count(S, m, n):
    # We need n+1 rows as the table is consturcted in bottom up
    # manner using the base case 0 value case (n = 0)
    table = [[0 for x in range(m)] for x in range(n+1)]
    # so now, we have (n+1)*m table for the dynamic programing, n=0 is the base case for the DP
 
    # Fill the enteries for 0 value case (n = 0)
    for i in range(m):       # m is  the total number of the coin types
        table[0][i] = 1      # init the base case for the DP table
 
    # Fill rest of the table enteries in bottom up manner
    for i in range(1, n+1):         # what is bottom up? from the right-bottom???, no, i j is from the 1 and 0, respectively
        for j in range(m):
            # Count of solutions including S[j], so S[j] decide the step size in the DP table???
            x = table[i - S[j]][j] if i-S[j] >= 0 else 0 # because only the base case is defined in the DP table, and the values are unknow in other areas
            # the new table [i][j] will base on previous values in the table 
 
            # Count of solutions excluding S[j], but include others, e.g., S[j-1] or S[j+1], etc ???
            y = table[i][j-1] if j >= 1 else 0
            #excluding S[j] means that it might use other coins as the solutions, so i keep unchange, while j-1
            # it is simliar to the method2: table[j] += table[j-S[i]], it should add with different coins
 
            # total count
            table[i][j] = x + y
 
    return table[n][m-1] # this save the final answer, this is the so-called bottom-up 
 
# Driver program to test above function
arr = [1, 2, 3]
m = len(arr)
n = 4
print(count(arr, m, n))

##method2, time: O(nm); space O(n)
# Dynamic Programming Python implementation of Coin 
# Change problem
def count(S, m, n):
 
    # table[i] will be storing the number of solutions for
    # value i. We need n+1 rows as the table is constructed
    # in bottom up manner using the base case (n = 0)
    # Initialize all table values as 0
    table = [0 for k in range(n+1)]
 
    # Base case (If given value is 0)
    table[0] = 1
 
    # Pick all coins one by one and update the table[] values
    # after the index greater than or equal to the value of the
    # picked coin
    for i in range(0,m): ### for-loop each stepsize to go through all map , and then add all maps together to get the final map with final results
        print "i",i
        for j in range(S[i],n+1):
            table[j] += table[j-S[i]]
            print table[j]
 
    return table[n] #the final result is the answer
 
# Driver program to test above function
arr = [1, 2, 3]
m = len(arr)
n = 4
x = count(arr, m, n)
#print (x)
###http://www.geeksforgeeks.org/dynamic-programming-set-7-coin-change/
