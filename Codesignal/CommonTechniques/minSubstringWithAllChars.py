def checkSubstring(string, subs):
    """
        Checks if every character of a substring is in a string
        Args:
            @string: string to check
            @subs: substring to use

        Return:
            True or False
    """
    for j in subs:
        if j not in string:
            return False
    return True


def minSubstringWithAllChars(s, t):
    """
        Finds the minimum consecutive substring of s that contains all
        characters of t

        Args:
            @s: string of lowercase letters
            @t: string with unique characters
        Return:
            The minimum consecutive substring of t in s
    """
    temp = res = ""
    subList = []
    for i in range(len(s)):
        temp = s[i]
        if t == temp:
            subList.append(temp)
        for j in range(i + 1, len(s)):
            temp += s[j]
            if checkSubstring(temp, t):
                subList.append(temp)
    if subList:
        res = subList[0]
    for sub in subList:
        if len(sub) < len(res):
            res = sub
    return res
