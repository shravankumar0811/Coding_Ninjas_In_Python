## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
i=1
k=n//2
j=k
c=1
while k>-1 and (2*i-1)<=n:
    print(" "*k,end="")
    print("*"*(2*i-1),end="")
    k=k-1
    i=i+1
    print()
i=i-2
while c<=j and i>0:
    print(" "*c,end="")
    print("*"*(2*i-1),end="")
    c=c+1
    i=i-1
    print()
