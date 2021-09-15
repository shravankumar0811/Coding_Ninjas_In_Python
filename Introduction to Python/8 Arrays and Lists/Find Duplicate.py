##Find Duplicate
##Send Feedback
##Given an integer array(ARR) of size N which contains numbers from 0 to (N - 2). Each number is present at least once. That is, if N = 5, the array constitutes values ranging from 0 to 3 and among these, there is a single integer value that is present twice. You need to find and return that duplicate number present in the array.
##Assume, duplicate number is always present in the given array.
##Input format :
##Line 1 : An integer N(size of the input array)
##Line 2 : Array elements (separated by a single space)
##Output Format :
##Duplicate element


## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
l=list(map(int,input().split()))
k=[0]*n
for i in l:
    k[i]+=1
for i in range(n-1):
    if k[i]==2:
        print(i)
    
