class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        temp = [0]*n
        j=0
        for i in range(n):
            if nums[i]!= 0:
                temp[j] = nums[i]
                j+=1
        nums[:] = temp
        