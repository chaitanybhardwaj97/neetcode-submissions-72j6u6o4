class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum_primary = 0
        sum_secondary = 0
        subtract = 0

        if len(mat) % 2 != 0:
            middle_i = len(mat)//2
            subtract = mat[middle_i][middle_i]
            print(subtract)


        for i in range(len(mat)):
            for j in range(len(mat)):
                if i==j:
                    sum_primary+=mat[i][j]

        print(sum_primary)

    
        for i in range(len(mat)):
            for j in range(len(mat)):
                if i+j == len(mat)-1:
                    sum_secondary+=mat[i][j]

        print(sum_secondary)

        return (sum_primary + sum_secondary - subtract)
