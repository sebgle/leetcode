# Last updated: 7/16/2025, 9:43:11 AM
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = ['/']
        periods = 0
        letters = False
        for c in path:
            if c == '/':
                if stack[-1] != '/':
                    if periods == 1 and not letters:
                        stack.pop()
                        stack.pop()
                        stack.append(c)
                    elif periods == 2 and not letters:
                        stack.pop()
                        stack.pop()
                        if len(stack) > 1:
                            count = 0
                            while count < 2:
                                if stack[-1] == '/':
                                    count += 1
                                stack.pop()
                            stack.append(c)
                    else:
                        stack.append(c)
                    periods = 0
                    letters = False
            elif c == '.':           
                periods += 1
                stack.append(c)
            else:
                stack.append(c)
                letters = True
                periods = 0
        if periods == 1 and not letters:
            stack.pop()
        elif periods == 2 and not letters:
            stack.pop()
            stack.pop()
            if len(stack) > 1:
                count = 0
                while count < 2 and len(stack) > 1:
                    if stack[-1] == '/':
                        count += 1
                    stack.pop()
        if stack[-1] == '/' and len(stack) > 1:
            stack.pop()
        return "".join(stack)