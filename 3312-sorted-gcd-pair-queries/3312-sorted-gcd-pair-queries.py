from typing import List
from bisect import bisect_right


class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        maximum = max(nums)

        frequency = [0] * (maximum + 1)

        for num in nums:
            frequency[num] += 1

        gcd_count = [0] * (maximum + 1)

        for g in range(maximum, 0, -1):
            divisible = 0

            for multiple in range(g, maximum + 1, g):
                divisible += frequency[multiple]

            gcd_count[g] = divisible * (divisible - 1) // 2

            for multiple in range(2 * g, maximum + 1, g):
                gcd_count[g] -= gcd_count[multiple]

        prefix = []
        total = 0

        for g in range(1, maximum + 1):
            total += gcd_count[g]
            prefix.append(total)

        ans = []

        for query in queries:
            ans.append(bisect_right(prefix, query) + 1)

        return ans