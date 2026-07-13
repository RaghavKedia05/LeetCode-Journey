class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        nums = "123456789"
        ans = []

        for length in range(len(str(low)), len(str(high)) + 1):
            for i in range(10 - length):
                num = int(nums[i:i + length])
                if low <= num <= high:
                    ans.append(num)

        return ans
        