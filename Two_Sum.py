from typing import List


# we want to make a hashmap of previously visited numbers: index
# for each visit, see if we can find the complement in the visited set and return the two indices
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in prev:
                return [index, prev[complement]]
            else:
                prev[num] = index
        return []
