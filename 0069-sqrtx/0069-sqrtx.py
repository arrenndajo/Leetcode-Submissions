class Solution:
    def mySqrt(self, x: int) -> int:
        first, last = 0, x
        result = 0

        while first <= last:
            mid = first + ((last - first) // 2)
            if mid**2 > x:
                last = mid - 1
            elif mid**2 < x:
                first = mid + 1
                result = mid
            else:
                return mid
        return result