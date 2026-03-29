# Greedy approach: list values and symbols from largest to smallest (including
# subtractive cases like CM=900, CD=400, IV=4). Repeatedly subtract the largest
# fitting value and append its symbol.
def intToRoman(num):
        symbols = [
            'M', 'CM', 'D', 'CD',
            'C', 'XC', 'L', 'XL',
            'X', 'IX', 'V', 'IV',
            'I']
        values = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1]
        
        roman = []
        for v, s in zip(values, symbols):
            while num >= v:
                num -= v
                roman.append(s)
        
        return ''.join(roman)


num = 58
print(intToRoman(num))