class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        targetSum = sum(nums) - x
        if targetSum < 0:
            return -1
        if targetSum == 0:
            return len(nums)
        
        i, s = 0, 0
        maxLength = -1

        for j, num in enumerate(nums):
            s += num
            
            while s > targetSum:
                s -= nums[i]
                i += 1
            
            if s == targetSum:
                maxLength = max(maxLength, j - i + 1)

        return maxLength if maxLength == -1 else len(nums) - maxLength

