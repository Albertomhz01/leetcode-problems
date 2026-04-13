# Last updated: 4/12/2026, 10:23:07 PM
from collections import Counter
class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        
        total = sum(nums)
        count = Counter(nums)
        result = float('-inf')

        visited = set()
        for i in range(len(nums)):
            if nums[i] in visited:
                continue
            visited.add(nums[i])

            # Treat nums[i] as the outlier
            remainder = total - nums[i]

            if remainder % 2 == 0:
                half = remainder // 2

                # Temporarily "remove" nums[i] from the pool
                count[nums[i]] -= 1

                # Check if half exists in the remaining elements
                if count.get(half, 0) > 0:
                    result = max(result, nums[i])

                count[nums[i]] += 1

        return result