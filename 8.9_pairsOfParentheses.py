###CCI6 8.9 n paris of balanced parentheses
def paranthesis(output = "", open = 0, close = 0, n = 1):
    if open == n and close == n:
        print "final output:", output , ','  #base case to stop
    else: # the common condition for the recursion, so it should use else for difference
        print "output1", output 
        if open < n: # so open can be 0, 1, 2, then will have 'c', 'cc', 'ccc', repectively,
            paranthesis(output + "(", open + 1, close, n) # this will also deploy the below command, e.g., when open+1=2
        
        print "open",open
        print "close",close
        if close < open: #not elif, they are parallel
            paranthesis(output + ")", open, close + 1, n) # this will also deploy the above command, e.g., when open=1
        # open<n and open+1 in the subfunc, it is just like a for-loop, so it will return back to open-1 for-loop

paranthesis(n = 3)
