# general framework for solving the calculator problem

# this questions is for calculator with +, -, *, /, and ()
# for division round to zero 


# key idea 
# two levels:
# - level 1: + and -; use l1 to keep level one result, and o1 to keep the operation; l1 = 0 to perform plus/minus opeeration; o1 = 1 as '+', -1 as '-'
# - level 2: * and /; use l2 to keep level one result, and o2 to keep the operation; l2 = 1 to perform product operation; o2 = 1 as '*', -1 as '/'


class Calculator:
    def __init__(self):
        self.i = 0

    def calculate(self, s: str) -> int:
        l1, o1 = 0, 1
        l2, o2 = 1, 1
        n = len(s)
        
        # Tracks if the next + or - could be a unary sign
        expect_unary = True 

        while self.i < n:
            c = s[self.i]

            if c == ' ':
                self.i += 1
                continue  # Skip spaces without resetting expect_unary

            elif c.isdigit():
                num = 0
                while self.i < n and s[self.i].isdigit():
                    num = num * 10 + int(s[self.i])
                    self.i += 1
                
                l2 = l2 * num if o2 == 1 else int(l2/num)
                expect_unary = False  # Next operator cannot be unary

            elif c == '(':
                self.i += 1
                num = self.calculate(s)
                l2 = l2 * num if o2 == 1 else int(l2/num)
                expect_unary = False  # The closing ')' just processed means next isn't unary
            
            elif c == ')':
                self.i += 1
                break

            elif c in ('+', '-'):
                # IF it's a unary sign, we apply it directly to the next upcoming number
                if expect_unary:
                    # We toggle the sign of l2 because l2 will be multiplied by the next number
                    if c == '-':
                        l2 = -l2
                    # Note: a unary '+' changes nothing, so we just skip it
                    self.i += 1
                else:
                    # Standard binary operator processing
                    l1 += l2 * o1
                    l2, o2 = 1, 1
                    o1 = 1 if c == '+' else -1
                    self.i += 1
                    expect_unary = True  # After a binary operator, a unary sign is possible
            
            elif c in ('*', '/'):
                o2 = 1 if c == '*' else -1
                self.i += 1
                expect_unary = True  # After a binary operator, a unary sign is possible

        return l1 + o1 * l2


c = Calculator()
#s = '2 + 3*5'
s = "10+(-2)*3"
print(c.calculate(s))


# s = '12 + (2 + 3*5) - 5'
# s = '3*5 + 2'
# s = '12/3'

