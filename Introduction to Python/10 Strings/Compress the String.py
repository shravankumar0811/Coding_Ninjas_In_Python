##Compress the String
##Send Feedback
##Write a program to do basic string compression. For a character which is consecutively repeated more than once, replace consecutive duplicate occurrences with the count of repetitions.
##For e.g. if a String has 'x' repeated 5 times, replace this "xxxxx" with "x5".
##Note : Consecutive count of every character in input string is less than equal to 9.
##
##
##Input Format :
##String S
##Output Format :
##Compressed string 


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
        c=c+1
    if c>1:
        y=y+s[i]+str(c)
    else:
        y=y+s[i]
    i=j
print(y)
