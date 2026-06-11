class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] not in "+-*/":
                stack.append(int(tokens[i]))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                if tokens[i]== '+':
                    stack.append(num1 + num2)
                if tokens[i]== '-':
                    stack.append(num2 - num1)
                if tokens[i]== '*':
                    stack.append(num2 * num1)
                if tokens[i]== '/':
                    stack.append(int(num2 / num1)) 
        return stack[-1]


