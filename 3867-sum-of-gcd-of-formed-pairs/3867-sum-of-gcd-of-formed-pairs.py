class Solution:
    def gcdSum(self, nums: list[int]) -> int:        
        prefixgcd=[]
        maximum=0
        for num in nums:
            maximum=max(maximum,num)
            prefixgcd.append(gcd(maximum,num))

        prefixgcd.sort()

        left=0
        right=len(nums)-1
        ans=0

        while left<right:
            ans += gcd(prefixgcd[left],prefixgcd[right])
            left+=1
            right-=1
        return ans
        
            