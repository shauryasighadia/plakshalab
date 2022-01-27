def isPalindrome(str):
    if type(str) == int or float:
        raise TypeError("enter a string")
    else:
        rev = ''.join(reversed(str))
        if (str == rev):
            return True
        else:
            return False

str = input("Enter a string")
ans = isPalindrome(str)
 
if (ans):
    print("It is a Palindrome")
else:
    print("It is not a Palindrome")