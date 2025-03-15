class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l, output = 0, 0
        for r, num in enumerate(nums):
            if num == 0:
                l = r + 1
            output = max(output, r-l+1)
        return output