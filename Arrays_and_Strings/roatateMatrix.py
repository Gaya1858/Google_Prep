from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i,len(matrix)):
                if i != j:
                    matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

        for i, num in enumerate(matrix):
           matrix[i] = list(reversed(num))

        print(matrix)
s =Solution()
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
s.rotate(matrix)