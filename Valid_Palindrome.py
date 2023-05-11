# two pointers approach, only compare when we have an alphanumeric value
# (alnum), if it's not the same if it is not the same then we can return a
# fail, if we make it through the whole thing we can return a true
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True
