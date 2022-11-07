#   69. Sqrt(x)

class Solution:
    def mySqrt(self, x: int) -> int:
        if not x:
            return 0
        l, r = 0, x
        while l <= r:
            m = (l + r) // 2
            if m ** 2 < x:
                l = m + 1
            elif m ** 2 > x:
                r = m - 1
            else:
                return m
        return r
      
      
      
      
def mySqrt(x):
    l, r = 0, x
    while l <= r:
        m = (r + l) // 2
        if x < m ** 2:
            r = m - 1
        elif x > m ** 2:
            l = m + 1
        else:
            return m
    return r
print(mySqrt(4))
print(mySqrt(49))
print(mySqrt(81))
print(mySqrt(8))
print(mySqrt(6))
