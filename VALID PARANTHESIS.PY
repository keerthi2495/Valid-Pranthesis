class Solution(object):
    def isValid(self, s):
        stack = []
        brackets = {')': '(', '}': '{', ']': '['}
        
        for i in s:
            if i in brackets.values():  # Opening brackets
                stack.append(i)
            else:  
                if not stack or brackets[i] != stack.pop():
                    return False  
                
        return len(stack) == 0  
