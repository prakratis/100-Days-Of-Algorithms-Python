from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        n = len(nums)
        for i in range(0,n):
            ans = target - nums[i]
            if ans in hash_map:
                return [hash_map[ans],i]
            else:
                hash_map[nums[i]] = hash_map.get(nums[i],i)