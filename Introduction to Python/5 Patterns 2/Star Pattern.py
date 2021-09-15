## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
for i in range(n):
    print(" "*(n-(i+1)),end="")
    print("*"*(i+1),end="")
    print("*"*i,end="")
    print()
    
