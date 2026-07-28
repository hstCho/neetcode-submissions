class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int):
        # Find the correct row
        left, right = 0, len(matrix) - 1
        row = 0
        while left <= right:
            mid = (left + right) // 2
            if matrix[mid][0] == target:
                return True
            if ((matrix[mid][0] < target and mid == len(matrix) - 1) 
                or (matrix[mid][0] < target and matrix[mid+1][0] > target)):
                row = mid
                break
            elif matrix[mid][0] > target:
                right = mid - 1
            else:
                left  = mid  + 1

        # Find the correct place within the row
        left, right = 0, len(matrix[row]) - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False
