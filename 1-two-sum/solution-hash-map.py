class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        map = {}
        for i in range(len(nums)):
            current = nums[i]
            complement = target - current
            if complement in map:
                return [map[complement], i]
            map[current] = i
        
        return []