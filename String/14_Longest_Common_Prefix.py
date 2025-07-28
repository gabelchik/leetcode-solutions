from typing import List


# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if len(strs) == 1:
#             return strs[0]
#         i, result = 0, ""
#         while i < len(strs[0]):
#             result += strs[0][i]
#             for j in range(1, len(strs)):
#                 if strs[j][:i+1] != result:
#                     return result[:i]
#             i+=1
#         return result

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        result = ""
        for i in range(min(len(strs[0]), len(strs[-1]))):
            if strs[0][i] != strs[-1][i]:
                return result
            result += strs[0][i]
        return result


solution = Solution()
strs = ["flower","fliger","flight"]
print(solution.longestCommonPrefix(strs))