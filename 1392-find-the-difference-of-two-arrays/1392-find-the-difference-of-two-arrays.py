class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1, set2 = set(nums1), set(nums2)
        res = [[], []]

        for n in set1:
            if n not in set2:
                res[0].append(n)
        
        for n in set2:
            if n not in set1:
                res[1].append(n)
        
        return res