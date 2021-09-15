##Push Zeros to end
##Send Feedback
##Given a random integer array, push all the zeros that are present to end of the array. The respective order of other elements should remain same.
##Change in the input array itself. You don't need to return or print elements. Don't use extra array.
##Note : You need to do this in one scan of array only.
##
##
##Input format :
##Line 1 : Integer N, Array Size
##Line 2 : Elements of the array separated by a single space.
##Output Format :
##Array elements in a single line (separated by single space)


## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
l=list(map(int,input().split()))
for i in l:
    if i!=0:
        print(i,end=" ")
x=l.count(0)
print("0 "*x)
