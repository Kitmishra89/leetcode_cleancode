class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        top, down = 0, len(matrix)
        left, right = 0, len(matrix[0])

        ans = list()

        total = down * right
        count = 0

        while count < total:
            for i in range(left, right):
                ans.append(matrix[top][i])
                count += 1
            top += 1
            print(ans)
            if count < total:
                for i in range(top, down):
                    ans.append(matrix[i][right-1])
                    count += 1
                right -= 1
            print(ans)

            if count < total:
                for i in range(right-1, left-1, -1):
                    ans.append(matrix[down-1][i])
                    count += 1
                down -= 1
            print(ans)

            if count < total:
                for i in range(down-1, top-1, -1):
                    ans.append(matrix[i][left])
                    count += 1
                left += 1
            print(ans)

        return ans
