##Write a Program to determine if the given number is Armstrong number or not. Print true if number is armstrong, otherwise print false.
##An Armstrong number is a number (with digits n) such that the sum of its digits raised to nth power is equal to the number itself.
##For example,
##371, as 3^3 + 7^3 + 1^3 = 371
##1634, as 1^4 + 6^4 + 3^4 + 4^4 = 1634
##Input Format :
##Integer n
##Output Format :
##true or false


def checkPalindrome(num):
    return num==num[::-1]

num = input()
isPalindrome = checkPalindrome(num)
if(isPalindrome):
	print('true')
else:
	print('false')
