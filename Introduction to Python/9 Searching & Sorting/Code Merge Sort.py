##Code Merge Two Sorted Arrays
##Send Feedback
##Given two sorted arrays of Size M and N respectively, merge them into a third array such that the third array is also sorted.
##Input Format :
## Line 1 : Size of first array i.e. M
## Line 2 : M elements of first array separated by space
## Line 3 : Size of second array i.e. N
## Line 2 : N elements of second array separated by space
##Output Format :
##M + N integers i.e. elements of third sorted array in a single line separated by spaces.



## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
l=list(map(int,input().split()))
m=int(input())
k=list(map(int,input().split()))
a=l+k
a.sort()
print(*a)
