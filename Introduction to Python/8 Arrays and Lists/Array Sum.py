##Array Sum
##Send Feedback
##Given an array of length N, you need to find and print the sum of all elements of the array.
##Input Format :
##Line 1 : An Integer N i.e. size of array
##Line 2 : N integers which are elements of the array, separated by spaces
##Output Format :
##Sum


## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
l=list(map(int,input().split()))
print(sum(l))
