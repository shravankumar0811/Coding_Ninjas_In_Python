##Print 2D array
##Send Feedback
##Given a 2D integer array with n rows and m columns. Print the 0th row from input n times, 1st row n-1 times…..(n-1)th row will be printed 1 time.
##Input format :
##
##Line 1 : No of rows(n) & No of columns(m) (separated by space)
##
##Line 2 : Row 1 elements (separated by space)
##
##Line 3 : Row 2 elements (separated by space)
##
##Line 4 : and so on
##
##Sample Input :
##3 3
##1    2    3
##4    5    6
##7    8    9
##Sample Output :
##1    2    3
##1    2    3
##1    2    3
##4    5    6
##4    5    6
##7    8    9



## Read input as specified in the question.
## Print output as specified in the question.
n,m=map(int,input().split())
for i in range(n):
    a=list(map(int,input().split()))
    for j in range(n-i):
        print(*a)
    
