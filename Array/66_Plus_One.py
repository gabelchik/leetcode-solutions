class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = -1
        while i >= -len(digits) and digits[i] == 9:
            digits[i] = 0
            i -= 1
        try:
            digits[i] +=1
        except IndexError:
            digits.insert(0, 1)

        return digits


# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         n = len(digits)
#         digits[-1] += 1
#         carry = digits[-1] > 9
#         digits[-1] %= 10
#
#         index = -1
#
#         while carry and n > -index:
#             index -= 1
#
#             digits[index] += 1
#             carry = digits[index] > 9
#             digits[index] %= 10
#
#         if carry:
#             digits.insert(0, 1)
#
#         return digits

