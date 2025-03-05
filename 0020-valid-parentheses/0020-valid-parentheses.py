class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")":"(", "]":"[", "}":"{" }

        # p stands for Parentheses
        for p in s:
            if p in closeToOpen: # refers to only key in the key:value pair
                if stack and stack[-1] == closeToOpen[p]:
                    stack.pop()
                else:
                    return False
            else: 
                stack.append(p)

        return True if not stack else False