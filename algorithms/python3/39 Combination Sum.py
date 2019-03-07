class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        current = []
        candidates.sort()

        def generate(numbers: List[int], target: int, threshold: int) -> None:
            for number in numbers:
                if number < threshold: continue
                if number == target:
                    current.append(number)
                    ans.append(current[:])
                    current.pop()
                    return
                if number < target:
                    current.append(number)
                    generate(numbers, target - number, number)
                    current.pop()
                if number > target:
                    return

        generate(candidates, target, -1)
        return ans