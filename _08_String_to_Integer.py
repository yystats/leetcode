"""
The algorithm for myAtoi(string s) is as follows:

1. Read in and ignore any leading whitespace.
2. Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. 
This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
3. Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
4. Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
5. If the integer is out of the 32-bit signed integer range [-2**31, 2**31 - 1], then clamp the integer so that it remains in the range. 
Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.
"""

def convertStringtoInt(s):
    sign = 1
    res = 0
    index = 0
    n = len(s)

    MAX_INT = 2**31 - 1
    MIN_INT = -2**31

    while index < n and s[index] == ' ':
        index += 1

    if index < n and s[index] == '+':
        sign = 1
        index += 1
    elif index < n and s[index] == '-':
        sign = -1
        index += 1

    while index < n and s[index].isdigit():
        digit = ord(s[index]) - ord('0')

        if (res > MAX_INT // 10) or (res == MAX_INT//10 and digit > MAX_INT % 10):
            return MAX_INT if sign == 1 else MIN_INT

        res = 10 * res + digit
        index += 1

    return sign * res


# example 

s = "4193 with words"
print(convertStringtoInt(s))

s = "   -42"
print(convertStringtoInt(s))

