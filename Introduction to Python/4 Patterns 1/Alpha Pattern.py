##Print the following pattern for the given N number of rows.
##Pattern for N = 3
## A
## BB
## CCC


## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
for i in range(n):
    for j in range(i+1):
        print(chr(65+i),end="")
    print()
