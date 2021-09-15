##Print the following pattern for the given N number of rows.
##Pattern for N = 4
##A
##BC
##CDE
##DEFG


## Read input as specified in the question
## Print the required output in given format
n=int(input())
for i in range(n):
    for j in range(i,i*2+1):
        print(chr(65+j),end="")
    print()
