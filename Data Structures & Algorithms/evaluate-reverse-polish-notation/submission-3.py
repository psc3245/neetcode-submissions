class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']
        for t in tokens:
            if (t in operators):
                r = stack.pop()
                l = stack.pop()
                if (t == '+'):
                    stack.append(int(l) + int(r))
                if (t == '-'):
                    stack.append(int(l) - int(r))
                if (t == '*'):
                    stack.append(int(l) * int(r))
                if (t == '/'):
                    stack.append(int(int(l) / int(r)))
            else:
                stack.append(t)
        return int(stack.pop())