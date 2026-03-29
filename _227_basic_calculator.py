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


# --- Test case for calculator(s): "32+2*2*2" => 40 ---
# Step-by-step walkthrough:
#   Initial: stack=[], num=0, sign='+'
#
#   i=0, char='3': digit → num = 0*10+3 = 3
#   i=1, char='2': digit → num = 3*10+2 = 32
#   i=2, char='+': operator → sign is '+', push 32 → stack=[32]. sign='+', num=0
#   i=3, char='2': digit → num = 0*10+2 = 2
#   i=4, char='*': operator → sign is '+', push 2 → stack=[32,2]. sign='*', num=0
#   i=5, char='2': digit → num = 0*10+2 = 2
#   i=6, char='*': operator → sign is '*', pop 2, push 2*2=4 → stack=[32,4]. sign='*', num=0
#   i=7, char='2': digit + last char → num = 0*10+2 = 2
#                   sign is '*', pop 4, push 4*2=8 → stack=[32,8]
#
#   return sum([32, 8]) = 40 ✓

s = "32+2*2*2"
print(calculator(s) == 40)  # True


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



