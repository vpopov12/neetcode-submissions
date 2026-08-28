class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lngSub = ""
        for i in range(len(strs[0])):
            n = strs[0][i]
            for word in strs[1:]:
                if i >= len(word) or word[i] != n:
                    return lngSub
            lngSub = lngSub + n
        return lngSub