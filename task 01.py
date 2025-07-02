import re

def is_palindrome(string):
    s = str(string)
    cleaned = re.sub(r'[^a-zA-Zа-яА-Я0-9]', '', s)
    cleaned = cleaned.lower()
    return cleaned == cleaned[::-1]

print(is_palindrome("A man, a plan, a canal -- Panama"))  
print(is_palindrome("А роза упала на лапу Азора"))        
print(is_palindrome("Madam, I'm Adam!"))                       
print(is_palindrome(333))                                 
print(is_palindrome("12321"))                                
print(is_palindrome(12345))
print(is_palindrome(None))
