class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count={}
        for num in nums:
            count[num]=count.get(num,0)+1
        duplicate=-1
        missing=-1
        for i in range(1,len(nums)+1):
            if count.get(i,0) >= 2:
                duplicate = i
            
            if count.get(i,0) == 0:
                missing = i
        return [duplicate,missing]


