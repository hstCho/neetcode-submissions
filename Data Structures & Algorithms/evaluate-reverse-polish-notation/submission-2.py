class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        int_stack = []
        operators = {'+', '-', '*', '/'}
        
        for i in range(len(tokens)):
            if tokens[i] in operators:
                sec = int_stack.pop()
                fir = int_stack.pop()
                op = tokens[i]
                if op == '+': res = fir + sec
                elif op == '-': res = fir - sec
                elif op == '*': res = fir * sec
                elif op == '/': res = int(fir / sec)
                print(fir, op, sec, '=', res)
            else:
                res = int(tokens[i])
            int_stack.append(res)
        
        return int_stack.pop()