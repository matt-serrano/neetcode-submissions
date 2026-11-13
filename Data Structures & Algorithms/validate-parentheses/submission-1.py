class Solution:
    def isValid(self, s: str) -> bool:
        p = {'}': '{', ')': '(', ']': '['}
        stack = []
        
        for i in s:
            if i not in p:
                stack.append(i)
            elif stack and stack[-1] == p[i]:
                stack.pop()
            else:
                return False
                
        return not stack