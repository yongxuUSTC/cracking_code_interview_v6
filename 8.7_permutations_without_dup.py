
class PermChar(object):
    
    def PermChar_noDup(self,chars):
        if len(chars)==1:
            return chars #stop case, return to the recursion subfunc, the final depth of the recur func without runing the
        # following main recursion;;; after this ,it is still in the same level
        
        #main recursion  
        result=[] #clear at each recursion
        for i in range(len(chars)):
            before=chars[:i]
            after=chars[(i+1):]
            cur=chars[i]
            subperms=self.PermChar_noDup(before+after) #sub-answer (for n-1)
            perms=[cur+perm for perm in subperms] #remains contain all of the sub (n-1) perms;; current answer
            result.extend(perms) # there is a for-loop outside, and it saves charsss, so it should "extend", not "append"
        return result # return the sub and final;;; after this it can return to the last level

def main():
    ts=PermChar()
    print ts.PermChar_noDup("abcd")

if __name__=='__main__':
    main()
