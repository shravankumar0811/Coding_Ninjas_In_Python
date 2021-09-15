##Fibonacci Member
##Send Feedback
##Given a number N, figure out if it is a member of fibonacci series or not. Return true if the number is member of fibonacci series else false.
##Fibonacci Series is defined by the recurrence
##    F(n) = F(n-1) + F(n-2)
##where F(0) = 0 and F(1) = 1
##
##
##Input Format :
##Integer N
##Output Format :
##true or false



def checkMember(n):
    a,b=0,1
    temp=0
    d=0
    while temp<n:
        temp=a+b
        a=b
        b=temp
        d=temp
    return d==n
        
        
n=int(input())
if(checkMember(n)):
    print("true")
else:
    print("false")
