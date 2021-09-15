##Spiral Print
##Send Feedback
##Given an N*M 2D array, print it in spiral form. That is, first you need to print the 1st row, then last column, then last row and then first column and so on.
##Print every element only once.
##Input format :
##Line 1 : N and M, No. of rows & No. of columns (separated by space) followed by N*M  elements in row wise fashion.
##Output format :
##Elements of matrix in spiral form in a single line and space separated
##
##
##Sample Input 1:
## 4 4 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
##Sample Output 1:
##1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10 
##Sample Input 2:
## 3 3 1 2 3 4 5 6 7 8 9
##Sample Output 2:
##1 2 3 6 9 8 7 4 5 



def opt_trans(arr):
    global m,n
    res=[[arr[j][i] for j in range(m)]for i in range(n)]
    m,n=n,m
    res=res[::-1]
   # print(res)
    return res

def spiralPrint(arr):
    global m,n
    res=[]
    while arr:
        res.append(arr[0])
        del arr[0]
        m-=1
        arr=opt_trans(arr)
    for ele in res:
        for s in ele:
            print(s,end=' ')

#Main
l=[int(i) for i in input().strip().split(' ')]
m, n=l[0], l[1]
arr = [ [ l[(j*n)+i+2] for i in range(n)] for j in range(m)]
spiralPrint(arr)
