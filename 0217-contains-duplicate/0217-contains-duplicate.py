class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Hashset: TC:O(n), SC:O(n)
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False