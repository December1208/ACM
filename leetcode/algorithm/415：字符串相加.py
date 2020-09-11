def countBinarySubstrings(s: str) -> int:
    last = 0
    length = len(s)
    i = 0
    result = 0
    while i < length:
        char = s[i]
        count = 0
        while i < length and s[i] == char:
            i += 1
            count += 1
        result += min(count, last)
        last = count
    return result


print(countBinarySubstrings("001101"))
