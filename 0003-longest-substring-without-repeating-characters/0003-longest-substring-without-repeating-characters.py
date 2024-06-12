class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a = s
        m = 0
        i = 0
        j = 0
        s1 = set()
        while j < len(a):
            if a[j] not in s1:
                s1.add(a[j])
                j += 1
                m = max(m, j - i)
            else:
                s1.remove(a[i])
                i += 1
        return m
                