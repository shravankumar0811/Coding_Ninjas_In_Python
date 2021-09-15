##Reverse Each Word
##Send Feedback
##Given a string S, reverse each word of a string individually. For eg. if a string is "abc def", reversed string should be "cba fed".
##Input Format :
##String S
##Output Format :
##Modified string


l=input().split()
k=[]
for i in l:
    k.append(i[::-1])
print(*k)
