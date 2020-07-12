class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        for size in range(len(arr), 1, -1):
            idx = arr.index(size)
            if idx == size - 1:
                continue
            if idx != 0:
                ans.append(idx + 1)
                arr[:idx + 1] = arr[:idx + 1][::-1]
            ans.append(size)
            arr[:size] = arr[:size][::-1]
        return ans
