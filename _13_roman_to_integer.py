# Pairwise comparison: iterate adjacent characters — if the current value is
# smaller than the next, subtract it (subtractive case, e.g. IV=4); otherwise
# add it. Always add the last character since it has no right neighbor.
def romanToInt(s):
    roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

    res = 0
    for a, b in zip(s, s[1:]):
        if roman[a] >= roman[b]:
            res += roman[a]
        else:
            res -= roman[a]
    
    res += roman[s[-1]]
    return res

s = 'LVIII'
print(romanToInt(s))