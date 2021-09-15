##Rotate array
##Send Feedback
##Given a random integer array of size n, write a function that rotates the given array by d elements (towards left)
##Change in the input array itself. You don't need to return or print elements.
##Input format :
##Line 1 : Integer n (Array Size)
##Line 2 : Array elements (separated by space)
##Line 3 : Integer d
##Output Format :
##Updated array elements in a single line (separated by space)


def Rotate(arr, d):
    return arr[d:]+arr[:d]
# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
d=int(input())
l=Rotate(arr, d)
print(*l)
