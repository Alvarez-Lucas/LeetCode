from typing import List


# The idea here is to use two pointers and calculate the maximum profit
# when the right pointer is smaller than the left, we have reached a new minimum and can move
# the left pointer to the right, if not, we can see if we have a new maximum, and we always want
# to move the right pointer
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProf = 0
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            else:
                maxProf = max(maxProf, prices[r] - prices[l])
            r += 1
        return maxProf
