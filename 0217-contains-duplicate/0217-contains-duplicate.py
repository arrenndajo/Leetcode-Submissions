class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Brute force: TC:O(n^2), SC:O(1) - Worst TC
        # Sort: TC:O(nlogn), SC:O(1) - Better TC

        # Hashset: TC:O(n), SC:O(n) - Best TC
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False