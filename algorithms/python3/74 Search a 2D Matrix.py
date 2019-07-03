class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0: return False
        m = len(matrix)
        n = len(matrix[0])
        if target < matrix[0][0] or target > matrix[m - 1][n - 1]: return False
        headList = []
        for i in range(m): 
            headList.append(matrix[i][0])
        rowIndex = binarySearch(headList, target, 0, m - 1, False)
        return binarySearch(matrix[rowIndex], target, 0, n - 1, True)

def binarySearch(arr: List, target: int, head: int, tail: int, equal: bool) -> int:
    print(head, tail, equal, arr)
    if tail - head <= 1:
        if equal:
            if arr[head] == target: return True
            if arr[tail] == target: return True
            return False
        else:
            if arr[head] <= target and (head == len(arr) - 1 or arr[head + 1] > target): return head
            if arr[tail] <= target and (tail == len(arr) - 1 or arr[tail + 1] > target): return tail
            return False

    t = math.floor((head + tail) / 2)
    if equal:
        if arr[t] == target:
            return True
    else:
        if arr[t] <= target and (t == len(arr) - 1 or arr[t + 1] > target):
            return t
    if arr[t] < target:
        return binarySearch(arr, target, t, tail, equal)
    if arr[t] > target:
        return binarySearch(arr, target, head, t, equal)