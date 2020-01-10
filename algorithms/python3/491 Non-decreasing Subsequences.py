class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = set()

        def backtrack(start, path):
            if len(path) >= 2:
                ans.add(tuple(path))
            for i in range(start, len(nums)):
                if not path or nums[i] >= path[-1]:
                    path.append(nums[i])
                    backtrack(i + 1, path)
                    path.pop()

        backtrack(0, [])
        return [list(seq) for seq in ans]
