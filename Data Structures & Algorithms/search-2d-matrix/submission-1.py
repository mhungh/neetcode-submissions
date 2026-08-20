class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        left, right = 0, rows * cols - 1

        while left <= right:
            mid = left + (right - left) // 2
            c = matrix[mid//cols][mid%cols]
            if c < target:
                left = mid + 1
            elif c > target:
                right = mid - 1
            else:
                return True
        
        return False