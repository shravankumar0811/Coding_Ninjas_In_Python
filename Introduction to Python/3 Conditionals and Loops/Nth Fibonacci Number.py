##Nth term of fibonacci series F(n) is calculated using following formula -
##    F(n) = F(n-1) + F(n-2), 
##    Where, F(1) = F(2) = 1
##Provided N you have to find out the Nth Fibonacci


## Read input as specified in the question.
## Print output as specified in the question.
def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
n=int(input())
print(fib(n))
