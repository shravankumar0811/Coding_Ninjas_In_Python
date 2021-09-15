##Pair Sum
##Send Feedback
##Given a random integer array(ARR) and a number X. Find and print the pair of elements in the array which sum to X.
##Given array can contain duplicate elements as well.
##While printing a pair, print the smaller element first.
##That is, if a valid pair is (6, 5) print "5 6". There is no constraint that out of 5 pairs which have to be printed in 1st line. You can print pairs in any order, just be careful about the order of elements in a pair.
##Input format :
##Line 1 : Integer N (size of the array)
##Line 2 : N elements of the Array separated by a single space.
##Line 3 : Integer X
##Output format :
##Line 1 : Pair 1 - Elements separated by a single space
##Line 2 : Pair 2 - Elements separated by a single space
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
