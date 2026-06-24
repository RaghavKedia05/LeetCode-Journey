class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        distinct = len(set(candyType))
        allowed = len(candyType)//2
        return min(distinct,allowed)
        