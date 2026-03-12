from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        n = len(nums)

        for i in range ( 0 , n ) :
            if nums[i] != val: 
                nums [j] = nums [i]
                j +=1
        return j