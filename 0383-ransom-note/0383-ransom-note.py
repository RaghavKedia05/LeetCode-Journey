class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count={}

        for ch in magazine:
            count[ch] = count.get(ch,0)+1

        for ch in ransomNote:
            if ch not in count:
                return False
            
            count[ch]-=1
        
            if count[ch]<0:
                return False

        return True
        