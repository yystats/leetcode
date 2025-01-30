'''
Given a string s which represents an expression, evaluate this expression and return its value. 
The integer division should truncate toward zero.
You may assume that the given expression is always valid. 

Example 1:

Input: s = "32+2*2*2"
Output: 40

'''

def calculator(s):
        s = s.replace(" ", "")  # Remove spaces
        stack = []
        num = 0
        sign = '+'  # Default sign
        
        for i, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)  # Build the number
                
            if char in "+-*/" or i == len(s) - 1:  # Process when an operator or last char
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    stack.append(int(stack.pop() / num))  # Truncate towards zero
                
                sign = char  # Update sign
                num = 0  # Reset number
        
        return sum(stack)  # Sum up the final stack values


s = "32       +2*2*2"
print(calculator(s) == 40)
