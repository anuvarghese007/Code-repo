def palindrome_func(s):
    #print(type(s))
    
    if not isinstance(s,str):
        s=str(s)
    if s[::-1] == s:
        return True
    else:
        return False

