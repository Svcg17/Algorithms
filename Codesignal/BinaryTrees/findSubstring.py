def findSubstrings(words, parts):
    """Finds the first and longest substring of @parts that exists in @word
    Example:
        words = ["Apple", "Melon", "Orange", "Watermelon"]
        parts = ["a", "mel", "lon", "el", "An"]
        Output -> ["Apple", "Me[lon]", "Or[a]nge", "Water[mel]on"]
    Args:
        words: array of strings to find parts
        parts: array of string that represent substrings
    Return: An array of strings based on words array where the
    substring is found
    """
    ret = []
    partsDict = {}

    for i in range(len(parts)):
        partsDict[parts[i]] = i

    for i in range(len(words)):
        longest = ""
        for s in range(len(words[i])):
            for e in range(s, len(words[i])):
                substr = words[i][s:e + 1]
                if substr in partsDict and len(substr) > len(longest):
                    longest = substr
        if longest:
            ret.append(words[i].replace(longest, "[{}]".format(longest), 1))
        else:
            ret.append(words[i])
    return ret
