class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = [[]]
        nums.sort()
        def generate(current: List[int], left: List[int]) -> None:
            for i in range(len(left)):
                t = left[i]
                current.append(t)
                results.append(current[:])
                generate(current, left[i + 1:])
                current.pop()

        generate([], nums)
        return results