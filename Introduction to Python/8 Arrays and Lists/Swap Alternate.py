##Swap Alternate
##Send Feedback
##Given an array of length N, swap every pair of alternate elements in the array.
##You don't need to print or return anything, just change in the input array itself.
##Input Format :
##Line 1 : An Integer N(size of the array)
##Line 2 : N integers which are elements of the array, separated by a single space
##Output Format :
##Elements after swapping in a single line, separated by a single space.


## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
l=list(map(int,input().split()))
for i in range(1,n,2):
    print(l[i],l[i-1],end=" ")
if n-i>1:
    print(l[i+1])
