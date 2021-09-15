##Print the following pattern for the given number of rows.
##Pattern for N = 5
##E
##DE
##CDE
##BCDE
##ABCDE


## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
for i in range(n):
    for j in range(i,-1,-1):
        print(chr(65+(n-j-1)),end="")
    print()
        
