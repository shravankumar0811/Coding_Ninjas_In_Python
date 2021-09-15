##Print the following pattern for the given number of rows.
##Pattern for N = 4
##1111
##000
##11
##0


## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
z=1
for i in range(n,-1,-1):
    for j in range(i):
        print(z,end="")
    if z==1:
        z=0
    else:
        z=1
    print()
            
