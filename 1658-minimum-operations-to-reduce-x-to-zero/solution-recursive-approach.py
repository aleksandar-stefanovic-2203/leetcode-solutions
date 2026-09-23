class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        def numOfOperations(nums: list[int], x: int, num: int) -> int:
            if x == 0:
                return num
            if x < 0:
                return -1
            if len(nums) == 0:
                return -1

            minLeft = numOfOperations(nums[1:], x - nums[0], num + 1)
            minRight = numOfOperations(nums[:-1], x - nums[-1], num + 1)

            if minLeft == -1 or minRight == -1:
                return max(minLeft, minRight)
            else:
                return min(minLeft, minRight)            

        return numOfOperations(nums, x, 0)
