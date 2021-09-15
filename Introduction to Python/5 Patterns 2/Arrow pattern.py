## Read input as specified in the question.
n=int(input())
i=1
j=0
while 2*i<=n and  j<n:
    print(" "*j,end="")
    for k in range(1,i+1):
        print("*",end=" ")
    i=i+1
    j=j+1
    print()
print(" "*j,end="")
for k in range(1,i+1):
    print("*",end=" ")
print()
j=j-1
i=i-1
while j>=0 and 2*i-1>0:
    print(" "*j,end="")
    for k in range(1,i+1):
        print("*",end=" ")
    i=i-1
    j=j-1
    print()
    
