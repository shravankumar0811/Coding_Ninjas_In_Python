##Sort 0 1
##Send Feedback
##You are given an integer array A that contains only integers 0 and 1. Write a function to sort this array. Find a solution which scans the array only once. Don't use extra array.
##You need to change in the given array itself. So no need to return or print anything.
##Input format :
##Line 1 : Integer N (Array Size)
##Line 2 : Array elements (separated by space)
##Output format :
##Sorted array elements in a single line separated by space



## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
l=list(map(int,input().split()))
l.sort()
print(*l)
