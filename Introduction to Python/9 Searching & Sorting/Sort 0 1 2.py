##Sort 0 1 2
##Send Feedback
##You are given an integer array containing only 0s, 1s and 2s. Write a solution to sort this array using one scan only.
##You need to change in the given array itself. So no need to return or print anything.
##Input format :
##Line 1 : Integer n (Array Size)
##Line 2 : Array elements (separated by space)
##Output Format :
##Updated array elements in a single line (separated by space)


## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
l=list(map(int,input().split()))
l.sort()
print(*l)
