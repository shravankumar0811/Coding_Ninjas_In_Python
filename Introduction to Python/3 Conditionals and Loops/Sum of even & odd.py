##Write a program to input an integer N and print the sum of all its even digits and sum of all its odd digits separately.



## Note : For printing multiple values in one line, put them inside print separated by space.
## You can follow this syntax for printing values of two variables val1 and val2 separaetd by space -
## print(val1, " ", val2)
l=list(input())
e,o=0,0
for i in l:
    if int(i)%2==0:
        o=o+int(i)
    else:
        e=e+int(i)
print(o,e,sep='   ')
