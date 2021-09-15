n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="",)
    print(" "*(2*n-2*i),end="")
    for k in range(i,0,-1):
        print(k,end="")
    print()
    
        
