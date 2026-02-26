#Brute Force Solution
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        r = k % n
        for _ in range (0 , r):
            e = nums.pop()
            nums.insert( 0 , e)