class Solution:
    def intToRoman(self, num: int) -> str:
        keyList = [["I", 1], ["IV", 4], ["V", 5], ["IX", 9],
                    ["X", 10], ["XL", 40], ["L", 50], ["XC", 90],
                    ["C", 100], ["CD", 400], ["D", 500], ["CM", 900],
                    ["M", 1000]]
                    
        result = "" 
        for key, val in reversed(keyList):
            if num // val != 0: 
                # eg: 1000/1000 = 1, it gets added to count.
                count = num // val
                result += (key * count)
                num = num % val
        return result