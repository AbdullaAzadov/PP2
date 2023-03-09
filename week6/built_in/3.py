def isPalindrome(txt):
    return txt == txt[::-1]

txt = input()

if isPalindrome(txt):
    print(txt,"is palindrome")
else:
    print(txt,"is not palindrome")