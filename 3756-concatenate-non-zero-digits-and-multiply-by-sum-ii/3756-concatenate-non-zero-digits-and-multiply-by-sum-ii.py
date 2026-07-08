class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)

        power = [1] * (n + 1)
        for i in range(1, n + 1):
            power[i] = power[i - 1] * 10 % MOD

        digitSum = [0] * (n + 1)
        nonZeroCount = [0] * (n + 1)
        prefixNum = [0] * (n + 1)

        for i in range(n):
            d = int(s[i])
            digitSum[i + 1] = digitSum[i] + d
            nonZeroCount[i + 1] = nonZeroCount[i] + (d != 0)

            if d != 0:
                prefixNum[i + 1] = (prefixNum[i] * 10 + d) % MOD
            else:
                prefixNum[i + 1] = prefixNum[i]

        ans = []

        for l, r in queries:
            count = nonZeroCount[r + 1] - nonZeroCount[l]
            total = digitSum[r + 1] - digitSum[l]

            x = (prefixNum[r + 1] - prefixNum[l] * power[count]) % MOD
            ans.append((x * total) % MOD)

        return ans
        