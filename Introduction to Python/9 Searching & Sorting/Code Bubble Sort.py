##Code Bubble Sort
##Send Feedback
##Given a random integer array. Sort this array using bubble sort.
##Change in the input array itself. You don't need to return or print elements.
##
##
##Input format :
##Line 1 : Integer N, Array Size
##Line 2 : Elements of the array separated by single space
##Output format :
##Elements of array in sorted order. Print them in a single line and space-separated




## Read input as specified in the question.
## Print output as specified in the question.
def bubbleSort(arr): 
    n = len(arr) 
    for i in range(n):
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
    print(*arr)
n=int(input())
l=list(map(int,input().split()))
bubbleSort(l)
