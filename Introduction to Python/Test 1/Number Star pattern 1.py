##Number Star pattern 1
##Send Feedback
##Print the following pattern for given number of rows.
##Input format :
##Integer N (Total number of rows)
##Output Format :
##Pattern in N lines
##Sample Input :
##   5
##Sample Output :
## 5432*
## 543*1
## 54*21
## 5*321
## *4321


## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
for i in range(1,n+1):
    for j in range(n,0,-1):
        if j==i:
            print("*",end="")
        else:
        	print(j,end="")
    print()
    
