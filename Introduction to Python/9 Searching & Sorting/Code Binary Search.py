##Code Binary Search
##Send Feedback
##Given a sorted integer array (in ascending order) and an element "VAL". You need to search this element "VAL" in the given input array using Binary Search. Return the index of element in the input.
##Indexing starts from 0.
##Return -1 if "VAL" is not present in the input array.
##
##
##Input format :
##Line 1 : Integer N, Array Size
##Line 2 : Elements of the array separated by single space
##Line 3 : Element to be searched (i.e. VAL)
##Output Format :
##Index of 'VAL' if found. Otherwise, '-1'



## Read input as specified in the question.
## Print output as specified in the questio
# Returns index of x in arr if present, else -1 
def binarySearch (arr, l, r, x): 
  
    # Check base case 
    if r >= l: 
  
        mid = l + (r - l)//2

        if arr[mid] == x: 
            return mid 
        
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 
  

        else: 
            return binarySearch(arr, mid+1, r, x) 
  
    else: 
        return -1
  
n=int(input())
l=list(map(int,input().split()))
x=int(input())
print(binarySearch(l,0,n,x))
