##Triplet Sum
##Send Feedback
##Given a random integer array(ARR) and a number X. Find and print the triplets of elements in the array which sum to X.
##While printing a triplet, print the smallest element first.
##That is, if a valid triplet is (6, 5, 10) print "5 6 10". There is no constraint that out of 5 triplets which have to be printed on 1st line. You can print triplets in any order, just be careful about the order of elements in a triplet.
##Input format :
##Line 1 : Integer N (size of the array)
##Line 2 : N elements of the Array separated by a single space.
##Line 3 : Integer X
##Output format :
##Line 1 : Triplet 1 - Elements separated by single space
##Line 2 : Triplet 2 - Elements separated by single space
##Line 3 : and so on


## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
l=list(map(int,input().split()))
k=int(input())
x=[]
j=n-1
for i in range(n):
    j=n-1
    while i<j:
        if l[i]+l[j]==k:
            x.append([l[i],l[j]])
        j=j-1
for i in x:
    i.sort()
    print(*i)
