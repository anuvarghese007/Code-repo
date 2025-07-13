def palindrome_func(val):
    if not isinstance(val, str):
         val = str(val)
    if val[::-1] == val:
        return True
    else:
        return False