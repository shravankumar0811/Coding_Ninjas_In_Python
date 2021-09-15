##Sum of two arrays
##Send Feedback
##Two random integer arrays are given A1 and A2, in which numbers from 0 to 9 are present at every index (i.e. single digit integer is present at every index of both given arrays).
##You need to find sum of both the input arrays (like we add two integers) and put the result in another array i.e. output array (output arrays should also contain only single digits at every index).
##The size A1 & A2 can be different.
##Note : Output array size should be 1 more than the size of bigger array and place 0 at the 0th index if there is no carry. No need to print the elements of output array.
##Input format :
##Line 1 : Integer n1 (A1 Size)
##Line 2 : A1 elements (separated by space)
##Line 3 : Integer n2 (A2 Size)
##Line 4 : A2 elements (separated by space)
##Output Format :
##Output array elements in a single line (separated by space)


## Read input as specified in the question.
## Print output as specified in the question.
a=int(input())
l=list(map(int,input().split()))
b=int(input())
k=list(map(int,input().split()))
x=""
y=""
for i in range(a):
    x=x+str(l[i])
for i in range(b):
    y=y+str(k[i])
#print(x,y)
z=str(int(x)+int(y))
print(0,end=" ")
for i in range(len(z)):
    print(z[i],end=" ")
