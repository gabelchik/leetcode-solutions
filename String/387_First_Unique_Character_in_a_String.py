# from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        all_chars = "abcdefghijklmnopqrstuvwxyz"

        m = float('+inf')
        for char in all_chars:
            idx = s.find(char)
            if idx != - 1 and s.rfind(char) == idx:
                m = min(m, idx)

        return m if m != float('+inf') else -1


# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         count = Counter(s)
#
#         for i, char in enumerate(s):
#             if count[char] == 1:
#                 return i
#         return -1


# from collections import Counter
#
#
# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         c = Counter(s)
#
#         for i in c:
#             if c[i] == 1:
#                 return s.index(i)
#
#         return -1

solution = Solution()
s = "loveleetcode"
print(solution.firstUniqChar(s))
