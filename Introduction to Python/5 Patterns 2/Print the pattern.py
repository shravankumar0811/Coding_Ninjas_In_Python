##Print the following pattern for the given number of rows.
##Pattern for N = 5
## 1    2   3    4   5
## 11   12  13   14  15
## 21   22  23   24  25
## 16   17  18   19  20
## 6    7    8   9   10
##
##Sample Input :
##4
##Sample Output :
## 1  2  3  4
## 9 10 11 12
##13 14 15 16
## 5  6  7  8






n=int(input())
temp=0
k=n//2
for i in range(1,k+1,1):
    s=1+(i-1)*2*n
    temp=s
    for p in range(s,s+n,1):
        print(p,end=' ')
    print()

if(n%2==1):
    i=n//2+1
    s=1+(i-1)*2*n
    for p in range(s,s+n,1):
        print(p,end=' ')
    print()
    
r=n//2
temp+=n
for i in range(1,r+1):
    for p in range(temp,temp+n):
        print(p,end=' ')
    temp-=2*n
    print()
