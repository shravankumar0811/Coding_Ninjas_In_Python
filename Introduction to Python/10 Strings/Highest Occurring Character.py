##Highest Occurring Character
##Send Feedback
##Given a string, S, find and return the highest occurring character present in the given string.
##If there are 2 characters in the input string with same frequency, return the character which comes first.
##
##
##Note : Assume all the characters in the given string are lowercase.
##
##
##Input format :
##String S
##Output format :
##Highest occurring character


## Read input as specified in the question.
## Print output as specified in the question.
s=input()
l=list(set(s))
k=[]
for i in l:
    k.append(s.count(i))
print(l[k.index(max(k))])
