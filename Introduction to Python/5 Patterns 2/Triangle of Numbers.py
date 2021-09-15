## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
s=""
for i in range(n):
    print(" "*(n-i-1),end="")
    for j in range(i+1,2*i+2):
        print(j,end="")
    for k in range(j-1,i,-1):
        print(k,end="")
    print()
