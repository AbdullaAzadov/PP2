def isPalindrome(string):
    r_string = "".join(reversed(string))
    if r_string == string:
        print(string, "is palindrome")
    else:
        print(string, "is NOT palindrome") 

word = input()
isPalindrome(word)           