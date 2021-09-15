##Check Palindrome
##Send Feedback
##Given a String s, check it its palindrome. Return true if string is palindrome, else return false.
##Palindrome strings are those, where string s and its reverse is exactly same.
##Input Format :
## String S
##Output Format :
##"true" if S is palindrome, else "false"


## Read input as specified in the question.
## Print output as specified in the question.
s=input()
if s==s[::-1]:
    print("true")
else:
    print("false")
