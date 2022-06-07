def longestSubstring(s):
    """
    Given a string s, find the length of the longest substring without repeating characters.
    """

    """
    Idea: sliding window
    - use dictionary to store the index and char 
    - search through the string, and if found in the dict and start <= found char index, re-position the start 
    """

    if len(s) <= 1:
        return len(s)

    start, maxLength = 0, 0
    dict = {}

    for i, c in enumerate(s):
        if c in dict and start <= dict[c]:
            start = dict[c] + 1
            maxLength = max(maxLength, i-start+1)

        dict[c] = i

    return maxLength 

# Run Test 
import unittest 

class TestStringMethods(unittest.TestCase):
    def test(self):
        s = "abcabcbb"
        res = longestSubstring(s)
        self.assertEqual(res, 3) 

if __name__ == '__main__':
    unittest.main()
