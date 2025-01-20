#You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.
#Time complexity: O(n) || Space complexity: O(n)

def evalRPN(tokens):
    stack = []
    for c in tokens:
        if c == '+':
            a, b = stack.pop(), stack.pop()
            stack.append(int(a + b))
        elif c == '-':
            a, b = stack.pop(), stack.pop()
            stack.append(int(a - b))
        elif c == '*':
            a, b = stack.pop(), stack.pop()
            stack.append(int(a * b))
        elif c == '/':
            a, b = stack.pop(), stack.pop()
            stack.append(int(a // b))
        else:
            stack.append(int(c))
    return stack.pop()

tokens=["2","1","+","3","*"]
print(evalRPN(tokens))