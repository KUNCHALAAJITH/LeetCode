class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        l=heights[:]
        a=sorted(heights)
        if l==a:
            return 0
        c=0
        for i in range(len(l)):
            if l[i]!=a[i]:
                c+=1
        return c
        