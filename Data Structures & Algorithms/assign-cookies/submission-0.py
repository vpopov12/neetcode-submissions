class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        g_counter, s_counter = 0,0
        g_cookies, s_cookies = len(g), len(s)
        while g_cookies > g_counter and s_cookies > s_counter:
            if g[g_counter] <= s[s_counter]:
                g_counter += 1
            s_counter += 1
        return g_counter