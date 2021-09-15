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
    
