def minRemoveToMakeValid(s):
    """
    Given a string s of '(' , ')' and lowercase English characters.
    Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.
    """

    """
    Key idea is to use Stack 

    Difficulty: Medium 
    Time: O(n)
    Space: O(n)
    """
    s = list(s)  # converst string into a list 
    stack = []   #  initialize an empty stack

    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)   # add the index of left parennthese
        elif c == ')':
            if stack:
                stack.pop()   # if find a pair match and stack is not none, pop 
            else:
                s[i] = ''

    # after completing the loop, stack might be non-empty, we need to set the char as blank
    while stack:
        s[stack.pop()] = ''

    return ''.join(s)

# testing 
import unittest

class TestStringMethod(unittest.TestCase):
    def check(self):
        s = "lee(t(c)o)de)"
        res = "lee(t(c)o)de"
        self.assertEqual(minRemoveToMakeValid(s), res)

if __name__ == '__main__':
    unittest.main()
