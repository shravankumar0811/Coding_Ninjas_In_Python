##Write a program that works as a simple calculator. It reads an integer for choice.
##1. If the choice is 1, 2 integers are taken for input and their sum is printed.
##2. If the choice is 2, 2 integers are taken for input and their difference is printed.
##3. If  the choice is 3, 2 integers are taken for input and their product is printed.
##4. If  the choice is 4, 2 integers are taken for input and their quotient is printed.
##5. If  the choice is 5, 2 integers are taken for input and their remainder is printed.
##6. If the choice is 6, the program exits, 
##For any other choice, print "Invalid Operation" and ask for choice again.




i=1
while i <= 7:
    choice=int(input())
    if choice==1:
        a=int(input())
        b=int(input())
        print(a+b)
    elif choice==2:
        a=int(input())
        b=int(input())
        print(a-b)
    elif choice==3:
        a=int(input())
        b=int(input())
        print(a*b)
    elif choice==4:
        a=int(input())
        b=int(input())
        print(a//b)
    elif choice==5:
        a=int(input())
        b=int(input())
        print(a%b)
    elif choice==6:
        exit()
    else:
        print("Invalid Operation")
    i=i+1
