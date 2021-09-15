##Check Permutation
##Send Feedback
##Given two strings, S and T, check if they are permutations of each other. Return true or false.
##Permutation means - length of both the strings should same and should contain same set of characters. Order of characters doesn't matter.
##Note : Input strings contain only lowercase english alphabets.
##
##
##Input format :
##Line 1 : String 1
##Line 2 : String 2
##Output format :
##'true' or 'false'


## Read input as specified in the question.
## Print output as specified in the question.
s=input()
c=0
ss=input()
for i in ss:
    if  i not in s:
        c=1
        break
if c==0:
    print("true")
else:
    print("false")
