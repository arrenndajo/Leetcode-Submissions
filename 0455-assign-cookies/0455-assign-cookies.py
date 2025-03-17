class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort() #sorting the 'greed factor'
        s.sort() #sorting the 'size of cookie'

        i = j = 0 
        while i < len(g): 
            while j < len(s) and g[i] > s[j]:
                j += 1
            if j == len(s):
                break
            i += 1
            j += 1
        return i