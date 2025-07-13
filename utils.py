def palindrome_func(val):
    curr = 0
    if isinstance(val, int):
         val = str(val)
    if val[::-1] == val:
        return True
    else:
        return False