class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        curSum = maxSum = nums[0]

        for i in range(0, len(nums) - 1):
            if nums[i] < nums[i+1]:
                curSum += nums[i+1]
            else:
                curSum = nums[i+1]
            maxSum = max(curSum, maxSum)
        
        return maxSum
