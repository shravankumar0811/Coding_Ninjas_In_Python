##Write a program to generate the reverse of a given number N. Print the corresponding reverse number.



n=int(input())
rev=0
p=n
while p!=0:
    r=p%10
    rev=rev*10+r
    p=p//10
print(rev)
