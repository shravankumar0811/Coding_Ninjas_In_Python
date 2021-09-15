##Print the following pattern for the given N number of rows.
##Pattern for N = 4
##1
##11
##111
##1111


## Read input as specified in the question.
## Print output as specified in the question.
## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
for i in range(n):
    for j in range(i+1):
        print("1",end="")
    print()
        
