class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        freq = {}
        windowSum = 0
        ans = 0

        for i in range(len(nums)):
            windowSum += nums[i]
            freq[nums[i]] = freq.get(nums[i], 0) + 1

            if i >= k:
                left = nums[i-k]
                windowSum -= left
                freq[left] -= 1
                if freq[left] == 0:
                    del freq[left]

            if i >= k-1 and len(freq) == k:
                ans = max(ans, windowSum)

        return ans

            
        