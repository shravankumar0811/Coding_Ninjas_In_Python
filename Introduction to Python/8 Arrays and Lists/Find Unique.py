##Find Unique
##Send Feedback
##Given an integer array of size 2N + 1. In this given array, N numbers are present twice and one number is present only once in the array.
##You need to find and return that number which is unique in the array.


n=int(input())
l=list(map(int,input().split()))
a=list(set(l))
for i in a:
    if l.count(i)==1:
        break
print(i)
