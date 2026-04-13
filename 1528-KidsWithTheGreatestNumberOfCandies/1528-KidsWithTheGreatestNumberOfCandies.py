# Last updated: 4/12/2026, 10:23:08 PM
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        max_value = max(candies)
        print(max_value)
        check = list()
        
        for ii in range(len(candies)):
            candies[ii] += extraCandies
            if candies[ii] >= max_value:
                check.append(True)
            else:
                check.append(False)
        
        return check
            