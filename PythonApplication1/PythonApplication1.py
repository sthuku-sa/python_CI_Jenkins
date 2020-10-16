print("This is to Check if a string is Palindrome --- for Continous Integration with jenkins and GitHub Test")

def isPalindrome(s):
    return s == s[::-1] #reverse the string --slice that steps backwards
 
s = "malayalam" #strint to reverse
print("String to reverse ", s)

ans = isPalindrome(s)
 
if ans:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")