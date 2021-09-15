##Write a program to determine if given number is palindrome or not. Print true if it is palindrome, false otherwise.



def checkPalindrome(num):
    return num==num[::-1]
		
num = input()
isPalindrome = checkPalindrome(num)
if(isPalindrome):
	print('true')
else:
	print('false')
