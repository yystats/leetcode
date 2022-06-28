def isValidPalindrome(s):
    """
    Given a string s, return true if the s can be palindrome after deleting at most one character from it.

    Input: s = "abca"
    Output: true
    Explanation: You could delete the character 'c'.

    """
    i, j = 0, len(s) - 1

    def isPalindrome(s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            else:
                i += 1
                j -= 1
        return True

    while i < j:
        if s[i] != s[j]:
            return isPalindrome(s, i+1, j) or isPalindrome(s, i, j-1)
        
        i += 1
        j -= 1

    return True


s = "abca"
print(isValidPalindrome(s))


