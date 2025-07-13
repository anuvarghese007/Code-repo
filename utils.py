def palindrome_func(s):
    #print(type(s))
    if isinstance(s,str):
        if s[::-1] == s:
            return True
        else:
            return False
    elif isinstance(s,int):
        if str(s)[::-1]==str(s):
            return True
        else:
            return False
