class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = set()
        for n in nums:
            if n not in hashmap:
                hashmap.add(n)
            else:
                return True
        return False