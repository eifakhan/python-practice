class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        a = max(candies)
        result = []
        for i in range(len(candies)):
            if a <= candies[i] + extraCandies:
                result.append(True)
            else:
                result.append(False)
        return result 
        

        