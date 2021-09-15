##Check Array Rotation
##Send Feedback
##Given an integer array, which is sorted (in increasing order) and has been rotated by some number k in clockwise direction. Find and return the k.
##Input format :
##Line 1 : Integer n (Array Size)
##Line 2 : Array elements (separated by space)
##Output Format :
##Integer k


## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
l=list(map(int,input().split()))
for i in range(n):
    if l[i+1]<l[i]:
        print(i+1)
        break
