def countBinarySubstrings(s: str) -> int:
    """
    给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。
    :param s:
    :return:
    """
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
