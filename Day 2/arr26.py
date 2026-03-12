#BRUTE FORCE SOLUTION
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        freq_map = {}

        for i in range(n):
            freq_map[nums[i]] = 1

        j = 0

        for key in freq_map:
            nums[j] = key
            j += 1

        return j
#OPTIMAL SOLUTION
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0:
            return 0

        i = 0  # slow pointer

        for j in range(1, n):  # fast pointer
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1