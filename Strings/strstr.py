def strstr(s, x):
    """
    Finds the first occurrence of x in s
    Args:
        s: string (haystack)
        x: string (needle)
    Return:
        The index in s of the first occurence of x, or -1 if not found.
    """
    if len(x) > len(s):
        return 0
    if x in s:
        return len(s.splt(x)[0])
    return -1

    """
    i = j = 0
    while i < len(s) and j < len(x):
        while i + 1 < len(s) and s[i] == s[i + 1]:
            i += 1
        if s[i] == x[j]:
            print(s[i])
            print(x[j])
            i += 1
            j += 1
        else:
            i += 1
            j = 0
    if j == len(x):
        return i - j
    return -1
    """
