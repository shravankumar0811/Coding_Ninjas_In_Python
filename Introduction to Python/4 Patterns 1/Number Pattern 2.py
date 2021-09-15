##Print the following pattern for the given N number of rows.
##Pattern for N = 4
##1
##11
##202
##3003


## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
for i in range(1,n+1):
    if i==1:
        print("1")
    elif i==2:
        print("11")
    else:
        print(str(i-1)+"0"*(i-2)+str(i-1))
