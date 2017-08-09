
###CCI6 8.8 Permutations with duplicates
class Perm_dup(object):
    
    def __init__(self):
        pass
    
    def permdup(self,chars):
        result=[]
        chars_count=self.count_chars(chars)
        #perms=self.permdup_helper('',chars_count,len(chars),result) #bug: this func not have any return values, the results are already in result
        #return perms 
        self.permdup_helper('',chars_count,len(chars),result)
        return result
    
    def permdup_helper(self, s, chars_count, n, result):
        if len(s)==n:  # n is the total length of ori string
            result.append(s) #stop case or base case
        
        for c in chars_count:
            
            #update the chars_count:
            if chars_count[c] == 1:
                del chars_count[c]
            elif chars_count[c] > 1:
                chars_count[c] -=1
            
            self.permdup_helper(s+c, chars_count, n, result)
            
            #recover the chars_count to support the next same level interation in the for-loop:
            if not c in chars_count:
                chars_count[c]=1
            elif c in chars_count:
                chars_count[c] += 1
    
    def count_chars(self,chars):
        chars_count={} #init a dict
        for item in chars:
            if not item in chars_count:
                chars_count[item]=1
            else:
                chars_count[item] += 1
        print chars_count
        return chars_count

def main():
    ts=Perm_dup()
    print ts.permdup('aaac')

if __name__=='__main__':
    main()
    
    ############################################################################################################
    # understanding helper comments below
    ###############################################
    import unittest
#  
# def perms_with_dups(s):
#     char_count = get_char_count(s)
#     result = []
#     perms_with_dups_helper('', char_count, len(s), result)
#     return result
#     
# def perms_with_dups_helper(s, char_count, n, result):
#     if len(s) == n:
#         print "stop, s",s
#         result.append(s)
#         
#     for char in char_count: # as the big high level loops, can regard them as independent big recursion
#         # this for can make sure that it traverses all possibilites, for is at which, the special which will come first order
#         
#         print "char",char
#         print "char_count1",char_count
#         if char_count[char] == 1:
#             del char_count[char] # del a key-val in the dict
#         else:
#             char_count[char] -= 1  
#         # del this cur char to add onto "s" step by step, untill 
#         
#         print "s",s
#         perms_with_dups_helper(s + char, char_count, n, result)
#  
#         print "s2",s
#         print "char2",char
#         if not char in char_count: # add back to the recursion
#             char_count[char] = 1
#         else:
#             char_count[char] += 1
#         print "char_count2",char_count #remember that there is a for-loop outside, it did not return to the last level imediately, but it returned to execute its brothers for the same level recursion
# ##like here:
# #s2 a
# #char2 a
# #char_count2 {'a': 1, 'c': 1}
# #char c
# #char_count1 {'a': 1, 'c': 1}
#  
#  
# def get_char_count(s):
#     char_count = {}  # def a dict with {}, not []
#     for char in s:
#         if char not in char_count:
#             char_count[char] = 1
#         else:
#             char_count[char] += 1
#             
#     print char_count
#     return char_count
#  
# class Test(unittest.TestCase):
#      
#     def setUp(self):
#         self.result = ['aaac', 'aaca', 'acaa', 'caaa']
#  
#     def test_perms_with_dups(self):
#         self.assertEqual(set(perms_with_dups('aaac')), set(self.result)) # the set can ignore the order of each item, this is important concept
#  
#  
# if __name__ == '__main__':
#     unittest.main()
