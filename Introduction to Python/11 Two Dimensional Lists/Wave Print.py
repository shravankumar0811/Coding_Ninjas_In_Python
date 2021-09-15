##Wave Print
##Send Feedback
##Given a two dimensional N*M array, print the array in a sine wave order. i.e. print the first column top to bottom, next column bottom to top and so on.
##Note : Print the elements separated by space.
##Input format :
##N, M, array elements (separated by space)
##Output format :
##Elements of matrix in wave form in a single line and space separated
##
##Sample Input 1:
##3 4 1  2  3  4 5  6  7  8 9 10 11 12
##Sample Output 1:
##1 5 9 10 6 2 3 7 11 12 8 4
##Sample Input 2:
##5 3 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
##Sample Output 2:
##1 4 7 10 13 14 11 8 5 2 3 6 9 12 15


l=[int(i) for i in input().split()]
m, n=l[0], l[1]
arr = [ [ l[(j*n)+i+2] for i in range(n)] for j in range(m)]
for i in range(n):
    k=[]
    for j in range(m):
        if i%2==0:
            print(arr[j][i],end=" ")
        else:
            k.append(arr[j][i])
    k=k[::-1]
    for _ in k:
        print(_,end=" ")
