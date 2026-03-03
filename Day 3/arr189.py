#Brute Force Solution:
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        r = k % n
        for _ in range (0 , r):
            e = nums.pop()
            nums.insert( 0 , e)

#Better Solution:
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = n % k
        nums[:] = nums [n-k :] + nums[ : n-k]

#Optimal Solution:
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n   # handle k > n

        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        # Step 1: reverse entire array
        reverse(0, n - 1)

        # Step 2: reverse first k elements
        reverse(0, k - 1)

        # Step 3: reverse remaining elements
        reverse(k, n - 1)
        