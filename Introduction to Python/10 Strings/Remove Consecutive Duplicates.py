##Remove Consecutive Duplicates
##Send Feedback
##Given a string, S, remove all the consecutive duplicates that are present in the given string. That means, if 'aaa' is present in the string then it should become 'a' in the output string.
##Input format :
##String S
##Output format :
##Modified string


## Read input as specified in the question.
## Print output as specified in the question.
s=input()
i=0
y=""
while i<len(s):
    x=s[i]
    j=i+1
    c=1
    while j<len(s) and s[j]==x:
        j=j+1
    y=y+s[i]
    i=j
print(y)
