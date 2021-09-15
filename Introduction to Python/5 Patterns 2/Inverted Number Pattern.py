##Print the following pattern for the given N number of rows.
##Pattern for N = 4
##4444
##333
##22
##1


## Read input as specified in the question
## Print the required output in given format
n=int(input())
for i in range(n,0,-1):
    for j in range(i):
        print(i,end="")
    print()
