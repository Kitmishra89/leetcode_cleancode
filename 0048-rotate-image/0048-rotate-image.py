class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        l, right = 0, len(matrix) - 1
        top, down = 0, right

        while l < right:
            for i in range(right-l):
                top, down = l, right

                temp = matrix[top][l+i]

                matrix[top][l+i] = matrix[down-i][l]
                matrix[down-i][l] = matrix[down][right-i]
                matrix[down][right-i] = matrix[top+i][right]
                matrix[top+i][right] = temp
                print(matrix)

            l += 1
            right -= 1
            