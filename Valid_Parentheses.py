# so the idea here is to iterate through the string and add chars to the stack
# popping characters from the stack when we find the closing one
# if the closing one doesn't match the top of the stack, its not in the right order
# we can fail early
# at the end, the stack should be empty or we can return a fail / False
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {"}": "{", "]": "[", ")": "("}
        for character in s:
            if character in closeToOpen:
                if stack and stack[-1] == closeToOpen[character]:
                    stack.pop(-1)
                else:
                    return False
            else:
                stack.append(character)
        return not stack


class SolutionOld:
    def isValid(self, s: str) -> bool:
        # a dictionary of closing to opening
        store = {"}": "{", "]": "[", ")": "("}
        stack = []
        for char in s:
            if char not in store:
                stack.append(char)
            else:
                if stack and stack[-1] == store[char]:
                    stack.pop(-1)
                else:
                    return False
        return not stack
