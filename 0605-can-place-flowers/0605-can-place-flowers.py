class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        extraFlowerBed = [0] + flowerbed + [0]

        for i in range(1, len(extraFlowerBed)-1): #skip first & last
            if extraFlowerBed[i-1] == 0 and extraFlowerBed[i] == 0 and extraFlowerBed[i+1] == 0:
                extraFlowerBed[i] = 1
                n -= 1
        return n <= 0