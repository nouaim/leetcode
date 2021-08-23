### https://leetcode.com/problems/find-kth-largest-xor-coordinate-value

class Solution:


    def kthLargestValue(self,matrix,k):


        m, n = len(matrix), len(matrix[0])
        arr = []
        for i in range(m):
            for j in range(n):
                if i: matrix[i][j] ^= matrix[i-1][j]
                if j: matrix[i][j] ^= matrix[i][j-1]
                if i and j: matrix[i][j] ^= matrix[i-1][j-1]
                arr.append(matrix[i][j])
        arr.sort()

        return arr[-k]

