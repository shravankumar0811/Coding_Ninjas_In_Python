##Array Intersection
##Send Feedback
##Given two random integer arrays(ARR1 and ARR2) of size M and N. You need to print their intersection; that is, an intersection is defined when both the arrays contain a particular value or to put it in other words when there is a common value in both the arrays.
##Input arrays can contain duplicate elements.
##Note : Order of the elements is not important
##
##
##Input format :
##Line 1 : An integer N(size of the first array)
##Line 2 : N elements of the array separated by a single space.
##Line 3 : An integer M(size of the second array)
##Line 4 : M elements of the array separated by a single space.
##Output format :
##Print the intersection elements on different lines


## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
l=list(map(int,input().split()))
m=int(input())
k=list(map(int,input().split()))
for i in range(n):
    if l[i] in k:
        z=k.index(l[i])
        k[z]=-100
        print(l[i])
        
