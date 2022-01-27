def isPalindrome(str):

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