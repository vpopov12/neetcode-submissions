class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap = Counter(s)

        for c in t:
            hashmap[c] -= 1
        for val in hashmap.values():
            if val != 0:
                return False
        return True