class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        def numOfOperations(nums: list[int], left: int, right: int, x: int, num: int) -> int:
            if x == 0:
                return num
            if x < 0:
                return -1
            if left > right:
                return -1

            minLeft = numOfOperations(nums, left + 1, right, x - nums[left], num + 1)
            minRight = numOfOperations(nums, left, right - 1,  x - nums[right], num + 1)

            if minLeft == -1 or minRight == -1:
                return max(minLeft, minRight)
            else:
                return min(minLeft, minRight)

        return numOfOperations(nums, 0, len(nums) - 1, x, 0)
