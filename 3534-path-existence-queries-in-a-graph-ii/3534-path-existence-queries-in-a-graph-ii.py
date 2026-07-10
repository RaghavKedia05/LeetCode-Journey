from typing import List
from bisect import bisect_right
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        order = sorted(range(n), key=nums.__getitem__)
        values = [nums[i] for i in order]

        pos = [0] * n
        for i, node in enumerate(order):
            pos[node] = i

        nxt = [bisect_right(values, values[i] + maxDiff) - 1 for i in range(n)]

        log = n.bit_length()
        up = [nxt]

        for _ in range(1, log):
            prev = up[-1]
            up.append([prev[prev[i]] for i in range(n)])

        ans = []

        for u, v in queries:
            left, right = pos[u], pos[v]

            if left > right:
                left, right = right, left

            if left == right:
                ans.append(0)
                continue

            steps = 0
            curr = left

            for k in range(log - 1, -1, -1):
                if up[k][curr] < right:
                    curr = up[k][curr]
                    steps += 1 << k

            ans.append(steps + 1 if nxt[curr] >= right else -1)

        return ans
        