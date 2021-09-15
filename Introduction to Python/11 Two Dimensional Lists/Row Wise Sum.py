##Row Wise Sum
##Send Feedback
##Given a 2D integer array of size M*N, find and print the sum of ith row elements separated by space.
##Input Format :
##Line 1 : Two integers M and N (separated by space) 
##Line 2 : Matrix elements of each row (separated by space)
##Output Format :
##Sum of every ith row elements (separated by space)
##
##Sample Input 1:
##4 2 
##1 2 3 4 5 6 7 8
##Sample Output 1:
##3 7 11 15 
##Sample Input 2:
##2 5 
##4 5 3 2 6 7 5 3 8 9
##Sample Output 2:
##20 32


m, n=(int(i) for i in input().strip().split(' '))
l=[int(i) for i in input().strip().split(' ')]
arr = [[ [ l[(j*n)+i] for i in range(n)] for j in range(m)]]
for i in arr:
    for j in i:
        print(sum(j),end=" ")
