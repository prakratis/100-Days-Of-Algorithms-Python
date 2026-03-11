#Brute Force Solution:
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range (0 , n+1):
            if i not in nums:
                return i
            
#Better Solution:
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        freq = {}
        for i in range ( 0 , n+1):
            freq[i] = 0
        
        for i in nums:
            freq[nums] = 1
        
        for k , v in freq.items():
            if v == 0:
                return k
        
#Optimal Solution:

