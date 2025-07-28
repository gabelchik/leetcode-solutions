from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()


solution = Solution()
s = ['h', 'i']
solution.reverseString(s)
print(s)
