##Print the following pattern for the given number of rows.
##Pattern for N = 4
##4444444
##4333334
##4322234
##4321234
##4322234
##4333334  
##4444444


n=int(input())
l=n*2-1
for i in range(l):
    for j in range(l):
        mi=min(i,j)
        mi=min(mi,l-i-1)
        mi=min(mi,l-j-1)
        print(n-mi,end="")
    print()
