from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)

        for i in range (0 , n):
             result ^= nums[i]
        
        return result