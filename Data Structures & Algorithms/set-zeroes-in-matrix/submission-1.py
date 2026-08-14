class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        first_row_zero = False
        first_col_zero = False

        # 1. Check whether the first row contains a zero
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_zero = True
                break

        # 2. Check whether the first column contains a zero
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True
                break

        # 3. Use first row/column as markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0  # mark row
                    matrix[0][j] = 0  # mark column

        # 4. Apply the markers to the rest of the matrix
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # 5. Handle the first row
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0

        # 6. Handle the first column
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0