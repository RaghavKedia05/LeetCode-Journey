class Solution:
    def minimumPushes(self, word: str) -> int:
        frequency = {}

        for ch in word:
            frequency[ch] = frequency.get(ch, 0) + 1

        counts = sorted(frequency.values(), reverse=True)

        ans = 0

        for i in range(len(counts)):
            pushes = i // 8 + 1
            ans += counts[i] * pushes

        return ans
        