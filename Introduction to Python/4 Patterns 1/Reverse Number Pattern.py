##Print the following pattern for the given N number of rows.
##Pattern for N = 4
##1
##21
##321
##4321


## Read input as specified in the question
## Print the required output in given format
n=int(input())
for i in range(n):
    for j in range(i+1,0,-1):
        print(j,end="")
    print()
