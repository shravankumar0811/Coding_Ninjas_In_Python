##Print the following pattern for a given n.
##For eg. N = 6
##123456
##  23456
##    3456
##      456
##        56
##          6
##        56
##      456
##    3456
##  23456
##123456



## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
i=1
k=0
while i<=n:
        print(" "*k,end="")
        k=k+1
        for j in range(i,n+1):
            print(j,end="")
        i=i+1
        print()
k=k-2
print(" "*k,end="")
i=i-2
while i>=1:
    for j in range(i,n+1):
        print(j,end="")
    i=i-1
    print()
    k=k-1
    print(" "*k,end="")
  
    
