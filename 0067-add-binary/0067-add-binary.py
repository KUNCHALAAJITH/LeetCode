class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, c, res, = 0, 0, ''
        while i < len(a) or i < len(b) or c:
            b1 = int(b[-i-1]) if i < len(b) else 0
            b2 = int(a[-i-1]) if i < len(a) else 0
            num = b1 + b2 + c
            res = str(num%2) + res
            c = 1 if num > 1 else 0
            i += 1
        return res
        