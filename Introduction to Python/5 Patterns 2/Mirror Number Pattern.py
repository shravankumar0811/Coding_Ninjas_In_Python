##Print the following pattern for the given N number of rows.
##Pattern for N = 4
##   1
##  12
## 123
##1234
##


## Read input as specified in the question
## Print the required output in given format
n=int(input())
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(1,i+1):
        print(k,end="")
    print()
    
