##Print the following pattern for the given N number of rows.
##Pattern for N = 4
##4444
##4444
##4444
##4444


## Read input as specified in the question
## Print the required output in given format
n=int(input())
for i in range(n):
    for j in range(n):
        print(n,end="")
    print()
