##Zeros and Stars Pattern
##Send Feedback
##Print the following pattern
##Pattern for N = 4
##*000*000*
##0*00*00*0
##00*0*0*00
##000***000
##Input Format :
##N (Total no. of rows)
##Output Format :
##Pattern in N lines
##Sample Input 1 :
##3
##Sample Output 1 :
##*00*00*
##0*0*0*0
##00***00
##Sample Input 2 :
##5
##Sample Output 2 :
##*0000*0000*
##0*000*000*0
##00*00*00*00
##000*0*0*000
##0000***0000



## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
l=[[0]*(2*n+1) for i in range(n)]
for i in range(n):
    for j in range(n):
        if i==j:
            l[i][j]="*"
for i in range(n):
    l[i][n]="*"
#print(l)
for i in range(n):
    for j in range(2*n+1):
        if i+j==2*n:
            l[i][j]="*"
for i in l:
    for j in i:
        print(j,end="")
    print()
    
