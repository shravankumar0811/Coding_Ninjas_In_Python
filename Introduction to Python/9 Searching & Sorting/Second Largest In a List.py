##Second Largest in array
##Send Feedback
##Given a random integer array of size n, find and return the second largest element present in the array.
##If n <= 1 or all elements are same in the array, return -2147483648 i.e. -2^31.
##Input format :
##Line 1 : Integer n (Array Size)
##Line 2 : Array elements (separated by space)
##Output Format :
##Second largest element



## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
l=list(map(int,input().split()))
s=list(set(l))
s.sort()
if len(s)<2:
    print("-2147483648")
else:
    print(s[-2])
