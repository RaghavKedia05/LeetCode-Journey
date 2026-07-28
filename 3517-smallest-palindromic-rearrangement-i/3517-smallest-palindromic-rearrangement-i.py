class Solution:
    def smallestPalindrome(self, s: str) -> str:
        left = sorted(s[:len(s)//2])
        middle = s[len(s)//2] if len(s)% 2 else ""
        return "".join(left)+middle+ "".join(reversed(left))
        

        