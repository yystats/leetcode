'''
Given a string s which represents an expression, evaluate this expression and return its value. 
The integer division should truncate toward zero.
You may assume that the given expression is always valid. 

Example 1:

Input: s = "32+2*2*2"
Output: 40

'''

'''
key idea: push to the stack once we see +-*/, and user another pointer to track the sign. 
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


# s = "32       +2*2*2"
# print(calculator(s) == 40)



### only + and *
def calculator2(expression):
    expression = expression.replace(" ", "")
    total = 0
    for add_term in expression.split('+'):
        product = 1
        for prod_term in add_term.split('*'):
            product *= int(prod_term)
        total += product
    return total

s = "5*9       +2*2*2 + 8*9"
print(calculator2(s))



