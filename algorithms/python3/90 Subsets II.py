class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        results = [[]]
        nums.sort()
        def generate(current: List[int], start: int) -> None:
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                current.append(nums[i])
                results.append(current[:])
                generate(current, i + 1)
                current.pop()
        generate([], 0)
        return results
