class Solution:
    def BS(self, vector: List[int], target: int) -> int:
        left = 0
        right = len(vector) - 1
        while (left <= right):
            mid = (left + right) //2
            if target == vector[mid]:
                return mid
            elif target < vector[mid]:
                right = mid - 1
            else:
                left = mid + 1
            mid = (right + left) /2
        return mid

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = []
        for elem in matrix:
            rows.append(elem[0])
        row_to_check = self.BS(rows, target)
        col_to_check = self.BS(matrix[int(row_to_check)], target)
        if matrix[int(row_to_check)][int(col_to_check)] == target:
            return True
        return False