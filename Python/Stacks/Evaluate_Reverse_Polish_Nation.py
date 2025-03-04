# Run command: python Evaluate_Reverse_Polish_Nation.py 

class Solution:
    def evalRPN(self, tokens):
        stack = []
        for c in tokens:
            if c == '+':
                a, b = stack.pop(), stack.pop()
                stack.append(int(a + b))
            elif c == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b - a))
            elif c == '*':
                a, b = stack.pop(), stack.pop()
                stack.append(int(a * b))
            elif c == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(c))
        return stack.pop()

# Example usage:
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
solution = Solution()
print(solution.evalRPN(tokens))