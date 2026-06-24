class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}

        for ch in s:
            count[ch] = count.get(ch,0) +1

        length = 0
        odd_occured = False
        for freq in count.values():
            if freq % 2 == 0:
                length+=freq
            else:
                length+=freq-1
                odd_occured=True
        if odd_occured:
            length+=1
        return length
        