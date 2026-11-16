class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            try:
                stack.append(int(i))
            except:
                int2 = stack.pop()
                int1 = stack.pop()

                if i == "+":
                    stack.append(int1 + int2)
                elif i == "-":
                    stack.append(int1 - int2)
                elif i == "*":
                    stack.append(int1 * int2)
                elif i == "/":
                    stack.append(int(int1 / int2))
                
        return stack[0]