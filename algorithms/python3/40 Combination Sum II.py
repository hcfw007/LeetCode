from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        current = []
        candidates.sort()

        def generate(numbers: List[int], target: int) -> None:
            for index in range(len(numbers)):
                number = numbers[index]
                if index > 0 and number == numbers[index - 1]: continue
                if number == target:
                    current.append(number)
                    ans.append(current[:])
                    current.pop()
                    return
                if number < target:
                    current.append(number)
                    _numbers = numbers[index + 1:]
                    generate(_numbers, target - number)
                    current.pop()
                if number > target:
                    return

        generate(candidates, target)
        return ans