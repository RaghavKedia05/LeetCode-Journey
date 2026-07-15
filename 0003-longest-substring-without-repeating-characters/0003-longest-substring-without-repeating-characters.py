class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ch = set()
        left = 0
        count = 0
        for right in range(0,len(s)):
            while s[right] in ch:
                ch.remove(s[left])
                left+=1

            ch.add(s[right])
            count = max(count,right-left+1)            
        return count
            
            
                
        


        