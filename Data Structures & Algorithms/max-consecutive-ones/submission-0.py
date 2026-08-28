class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        conMax = 0
        curMax = 0

        for n in nums:
            if n != 1:
                curMax = 0
            else: 
                curMax += 1
            conMax = max(conMax, curMax)
        return conMax