class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)//2):
            for j in range(i, len(matrix)-1-i):
                l, r, k = i, j, 0
                current = matrix[l][r]
                while k < 4:
                    if k == 0:
                        l += j - i
                        r += len(matrix) - 1 - j - i
                    elif k == 1:
                        l += len(matrix) - 1 - j - i
                        r = r - j + i
                    elif k == 2:
                        l = l - j + i
                        r = r - (len(matrix) - 1 - i) + j
                    elif k == 3:
                        l = l - (len(matrix) - 1 - i) + j
                        r += j - i
                    matrix[l][r], current = current, matrix[l][r]
                    k+=1
