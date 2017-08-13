# # A Python program to print all anagarms together
#  
# # structure for each word of duplicate array
# class Word(object):
#     def __init__(self, string, index):
#         self.string = string
#         self.index = index
# 
# #this concept is important, as it is just like a class
# 
#  
# # Create a DupArray object that contains an array
# # of Words
# def createDupArray(string, size):
#     dupArray = []
#  
#     # One by one copy words from the given wordArray
#     # to dupArray
#     for i in xrange(size):
#         dupArray.append(Word(string[i], i)) #dupArray contains the each Word class object
#  
#     return dupArray
#  
# # Given a list of words in wordArr[]
# def printAnagramsTogether(wordArr, size):
#     # Step 1: Create a copy of all words present in
#     # given wordArr.
#     # The copy will also have orignal indexes of words
#     dupArray = createDupArray(wordArr, size)
#  
#     # Step 2: Iterate through all words in dupArray and sort
#     # individual words.
#     for i in xrange(size):
#         dupArray[i].string = ''.join(sorted(dupArray[i].string))
#  
#     # Step 3: Now sort the array of words in dupArray
#     dupArray = sorted(dupArray, key=lambda k: k.string) # k is the Word class defined above, string is the "string"
#  
#     # Step 4: Now all words in dupArray are together, but
#     # these words are changed. Use the index member of word
#     # struct to get the corresponding original word
#     for word in dupArray:
#         print wordArr[word.index],
#  
# # Driver program
# wordArr = ["cat", "dog", "tac", "god", "act"]
# size = len(wordArr)
# printAnagramsTogether(wordArr, size)

### CCI6 10.2 Group Anagrams by myself

class Word(object): # this is like a struct to store two items together
    def __init__(self, string, index): # this is the construction method
        self.string=string
        self.index=index

class Word2(object): # this is like a struct to store two items together
    def __init__(self, num, index): # this is the construction method
        self.num=num
        self.index=index

def printAnagramsTogether(wordArr,size):
    dupArr=[]
    for i in range(size):
        dupArr.append(Word(sorted(wordArr[i]),i))
    
    dupArr=sorted(dupArr,key=lambda k : k.string)
    
    for word in dupArr:
        print wordArr[word.index]
        
def printAnagramsTogether_method2(wordArr,size):
    #method2: char-num-add & dict with several values

    dupArr_hash={}  # initi a dict
    dupArr_num=str_sum(wordArr)
    for i in range(size):
        if dupArr_num[i] not in dupArr_hash: #check key wether in the dict
            dupArr_hash[dupArr_num[i]]=[i]  # this is important, it is a '[i]', not 'i'; if it is 'i', it can not use 'append' later since it is an 'int', only a list can use 'append'
        elif dupArr_num[i] in dupArr_hash:
            dupArr_hash[dupArr_num[i]].append(i) # the para of append can be an int, or a list, will be appended as a whole
           #dupArr_hash[dupArr_num[i]].extend([i]) # the para of extend should be a list, not an int;;; the para of extend should be iterable, like a list;;; it should be an iterable object, split first and then merge for each item
    
    print dupArr_hash
    for k in dupArr_hash.keys(): #for-loop keys
        for ind in dupArr_hash[k]:
            print wordArr[ind]
        

def str_sum(wordArr):
    str_sum=[0 for i in range(len(wordArr))]
    for i in range(len(wordArr)):
        for ch in wordArr[i]:
            str_sum[i] += ord(ch)
    print str_sum
    return str_sum
    
#driver program
wordArr=["cat","dog","tac","god","act"]
size=len(wordArr)
print "\nmethod1 results:"
printAnagramsTogether(wordArr,size)
print "\nmethod2 results:"
printAnagramsTogether_method2(wordArr,size)
