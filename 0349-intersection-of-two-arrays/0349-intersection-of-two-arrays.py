class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = {}
        for num in nums1:
            count[num] = count.get(num,0)+1

        ans=[]
        for num in nums2:
            if num in count:
                if count[num]>0:
                    ans.append(num)
                    count[num]-= 1
        
        return list(set(ans))
        