def est_palindrome(s):
    if len(s) <= 1:
        return True
    
    if s[0] == s[-1]:
       return est_palindrome(s[1:-1])

    return False 

s= "radar"

print(est_palindrome(s))    
m="najat"
print(est_palindrome(m))