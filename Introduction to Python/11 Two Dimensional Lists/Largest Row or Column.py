##Largest Row or Column
##Send Feedback
##Given an NxM 2D array, you need to find out which row or column has largest sum (sum of its elements) overall amongst all rows and columns.
##Input Format :
## Line 1 : 2 integers N and M respectively, separated by space 
## Line 2: Single line having N*M elements entered in row wise manner, each separated by space.
##Output Format :
## If row sum is maximum then - "row" row_num max_sum
## If column sum is maximum then - "column" col_num max_sum


def largestRowCol(arr):

    max=-1

    flag=0

    r_i=-1

    c_i=-1

    res=[]

    for ele in arr:

        temp=sum(ele)

        if temp>max:

            max=temp

            r_i=arr.index(ele)

            flag=1

    for i in range(n):

        temp=0

        for j in range(m):

            temp+=arr[j][i]

        if temp>max:

            max=temp

            c_i=i

            flag=2

    if flag==1:

        res.append('row '+str(r_i)+' '+str(max))

    else:

        res.append('column '+str(c_i)+' '+str(max))

    return res

m, n=(int(i) for i in input().strip().split(' '))

l=[int(i) for i in input().strip().split(' ')]

arr = [ [ l[(j*n)+i] for i in range(n)] for j in range(m)]

l=largestRowCol(arr)

print(*l)
