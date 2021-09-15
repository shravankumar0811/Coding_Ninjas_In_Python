##Remove character
##Send Feedback
##Given a string and a character x. Write a function to remove all occurrences of x character from the given string.
##Leave the string as it is, if the given character is not present in the string.
##
##
##Input Format :
##Line 1 : String S
##Line 2 : Character c
##Output Format :
##Modified string

## Read input as specified in the question.
## Print output as specified in the question.
s=input()
a=input()
x=""
for i in s:
    if i!=a:
        x=x+i
print(x)
