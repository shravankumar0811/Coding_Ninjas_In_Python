##Palindrome number
##Send Feedback
##Write a program to determine if given number is palindrome or not. Print true if it is palindrome, false otherwise.
##Palindrome are the numbers for which reverse is exactly same as the original one. For eg. 121
##Sample Input 1 :
##121
##Sample Output 1 :
##true


def checkPalindrome(num):
    return num==num[::-1]

num = input()
isPalindrome = checkPalindrome(num)
if(isPalindrome):
	print('true')
else:
	print('false')
