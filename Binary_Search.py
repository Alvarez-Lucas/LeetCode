from typing import List


# The idea here is to make pointers to the left and right ends of the list of nums
# Then binary search
# Check the middle value
# if its bigger than we want, the value has to be to the left,
# so we move the right pointer to the middle
# if its smaller than we want, the value has to be to the right,
# so we move the left pointer to the middle
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = left + ((right - left) // 2)

            if nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                return middle

        return -1
