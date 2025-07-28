class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        if x[0] == '-':
            x = '-'+ x[1:][::-1]
        else:
            x = x[::-1]
        if -(2**31) <= int(x) <= 2**31 - 1:
            return int(x)
        else:
            return 0


solution = Solution()
s = -123
print(solution.reverse(s))
