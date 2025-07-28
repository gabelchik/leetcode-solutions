class Solution:
    def myAtoi(self, s: str) -> int:
        #1 этап
        s = s.lstrip()
        if not s:
            return 0
        num, sign, i = 0, 1, 0
        #2 этап
        if s[0] == '-':
            sign = -1
            i+=1
        elif s[0] == '+':
            i+=1
        #3 этап
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i+=1
        #4 этап
        if sign * num > 2**31-1:
            return 2**31 - 1
        elif sign* num < -2**31:
            return -2**31
        else:
            return sign * num




solution = Solution()
s = " "
print(solution.myAtoi(s))